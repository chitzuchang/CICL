"""cicl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from .views import GetAllDocumentAPIView, DocumentAPIView, MainPage

urlpatterns = [
    # Main Page URL
    path('', MainPage, name='index'),

    # Admin URLs
    path('admin/', admin.site.urls),

    # Document URLs
    url(
        r'^document/get/$',
        GetAllDocumentAPIView.as_view(),
        name='get_document'
        ),
    path(
        'document/get/<uuid:pk>',
        DocumentAPIView.as_view(),
        name='document'
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
