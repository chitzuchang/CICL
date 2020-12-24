# Backend

- Python 3.9
- Django 3.1.2

## Project setup

```
pip install -r requirements.txt
```

### Compiles static files for production

```
./manage.py collectstatic
```

### Create superuser for application

```
./manage.py createsuperuser
```

### Run a local server

```
./manage.py runserver
```

# Frontend

- Vue 2.6.11

## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn serve
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

# Deployment Instructions (Ubuntu 18.04+)

Based on a tutorial found on [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

## Installing the Packages from the Ubuntu Repositories

1. Ubuntu updates and Python 3.9 installation:

   ```Shell
   sudo apt update
   sudo apt install wget software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt install python3-pip python3.9-dev nginx curl
   ```

2. Installing Yarn:

   ```Shell
   sudo apt remove cmdtest
   sudo apt remove yarn
   curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
   echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
   sudo apt-get update
   sudo apt-get install yarn -y
   ```

## Creating a Python Virtual Environment

1. `sudo -H pip3 install --upgrade pip`
2. `sudo -H pip3 install virtualenv`
3. `mkdir ~/CICL`
4. `cd ~/CICL`
5. `virtualenv ciclvenv --python=python3.9`
6. `source ciclvenv/bin/activate`
7. `python -m pip install --upgrade pip`
8. `git clone https://github.com/chitzuchang/CICL.git`
9. `pip install -r requirements`
10. `yarn install`

## Configuring Django/Vue Project

1. `yarn build`
2. Create .env file with necessary environment variables (SECRET_KEYS, PASSWORDS, etc...)
   ```
   SECRET_KEY='...'
   PASSWORD='...'
   ```
3. `./manage makemigrations`
4. `./manage migrate`
5. `./manage createsuperuser`
6. `./manage collectstatic`

## Create systemd Socket and Service Files for Gunicorn

1. `sudo nano /etc/systemd/system/gunicorn.socket`

   ```
   [Unit]
   Description=gunicorn socket

   [Socket]
   ListenStream=/run/gunicorn.sock

   [Install]
   WantedBy=sockets.target
   ```

2. `sudo nano /etc/systemd/system/gunicorn.service`

   ```
   [Unit]
   Description=gunicorn daemon
   Requires=gunicorn.socket
   After=network.target

   [Service]
   User=username
   Group=www-data
   WorkingDirectory=/home/username/CICL
   EnvironmentFile=/home/username/CICL/.env
   ExecStart=/home/username/CICL/ciclvenv/bin/gunicorn \
          --chdir /home/username/CICL \
          --access-logfile - \
          --workers 8 \
          --bind unix:/run/gunicorn.sock \
          cicl.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

3. We can now start and enable the Gunicorn socket:

   ```Shell
   sudo systemctl start gunicorn.socket
   sudo systemctl enable gunicorn.socket
   ```

4. Check status of the gunicorn socket
   `sudo systemctl status gunicorn.socket`

5. Check existence of the gunicorn.sock file
   `file /run/gunicorn.sock`
   Output: /run/gunicorn.sock: socket

## Testing Socket Activation

1. `sudo systemctl status gunicorn`

2. Test if a curl command works:
   `curl --unix-socket /run/gunicorn.sock localhost`
   It return HTML output.

If you experience errors here then check the gunicorn socket logs:
sudo journalctl -u gunicorn.socket 3. After making changes make sure to run these commands:

```Shell
sudo systemctl daemon-reload
sudo systemctl restart gunicorn
```

## Configuring NGINX to Proxy Pass to Gunicorn

1. Create and open a new server block:
   sudo nano /etc/nginx/sites-available/myproject

   ```Shell
   server {
       listen 80;
       server_name server_domain_or_IP;

       location = /favicon.ico { access_log off; log_not_found off; }
       location /static/ {
           root /home/username/CICL/;
       }

       location / {
           include proxy_params;
           proxy_pass http://unix:/run/gunicorn.sock;
       }
   }
   ```

2. Enable the file by linking it to the sites-enabled directory:

   ```Shell
   sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
   ```

3. Restart Nginx
   ```Shell
   sudo systemctl restart nginx
   ```
