<template>
  <div class="hero-body">
    <div class="container">

      <div class="columns is-centered">
        <div class="column is-one-quarter">
          <b-input placeholder="Location"></b-input>
        </div>
        <div class="column is-one-quarter">
          <b-input placeholder="Core Name"></b-input>
        </div>
      </div>

      <div class="columns is-centered">
        <div class="column is-offset-one-quarter is-half">
          <b-input placeholder="Search..."></b-input>
        </div>
        <div class="column">
          <button class="button is-info is-bold">Search</button>
        </div>
      </div>

      <div class="column">
        <section>
          <b-table
            :data="data"
            :loading="loading"
            hoverable
            paginated
            backend-pagination
            :total="total"
            :per-page="perPage"
            :opened-detailed="defaultOpenedDetails"
            detailed
            detail-key="document_id"
            :show-detail-icon="showDetailIcon"
            @page-change="onPageChange"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
          >

            <b-table-column label="Core Name" v-slot="props">
              {{ props.row.core_name }}
            </b-table-column>
            <b-table-column
              field="Location"
              label="Location"
              v-slot="props"
            >
              {{ props.row.location }}
            </b-table-column>

            <b-table-column
              field="Parameters"
              label="Parameters"
              v-slot="props"
            >
              {{ props.row.parameters }}
            </b-table-column>

            <b-table-column label="Download" v-slot="props">
              <b-button 
              @click.prevent="downloadFile(`${props.row.document_file}`)"
              icon-left="file-download" 
              download>
              </b-button>
            </b-table-column>

            <template slot="detail" slot-scope="props">
              <article class="media">
                <div class="media-content">
                  <div class="content">
                    <p>
                      Researchers:
                      <ul>
                        <li v-for="r in props.row.researchers" :key="r">
                          {{ r.first_name }} {{ r.last_name }}
                        </li>
                      </ul>
                      Isotopes:
                      <ul>
                        <li v-for="i in props.row.isotopes" :key="i">
                          {{ i.name }} {{ i.symbol }}
                        </li>
                      </ul>
                      Parameters:
                      <ul>
                        <li v-for="p in props.row.parameters" :key="p">
                          {{ p.type }}
                        </li>
                      </ul>
                      Description:<br>
                      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                      Proin ornare magna eros, eu pellentesque tortor vestibulum ut.
                      Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.
                    </p>
                  </div>
                </div>
              </article>
            </template>
          </b-table>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      total: 0,
      loading: false,
      page: 1,
      perPage: 1,
      defaultOpenedDetails: [1],
      showDetailIcon: true,
    };
  },
  methods: {
    loadAsyncData() {
      const params = [
        `limit=1`,
        `offset=${this.page - 1}`,
      ].join("&");

      this.$http
      .get(`http://localhost:8000/document/get?${params}`)
      .then(({data}) => {
        this.data = [];
        data.results.forEach((item) => {
          this.data.push(item);
        });

        let totalCount = data.count;
        this.total = totalCount;
        this.loading = false;
      })
      .catch((error) => {
        this.data = [];
        this.total = 0;
        this.loading = false;
        throw error;
      });
    },

    onPageChange(page) {
      this.page = page;
      this.loadAsyncData();
    },

    downloadFile(url) {
      const filename = url.split('/').pop()

      this.$http
      .get(url, { responseType: 'blob' })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data], {
          type: 'application/vnd.ms-excel'
        }))
        const link = document.createElement('a');

        link.href = url;
        link.setAttribute('download', filename);
        document.body.appendChild(link);

        link.click();
      });
    },
  },

  mounted() {
    this.loadAsyncData();
  },
}
</script>