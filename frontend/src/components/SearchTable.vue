<template>
  <div class="hero-body">
    <div class="container">
      <form v-on:submit: @submit.prevent="onSearch">
        <div class="columns is-mobile is-centered">
          <div class="column is-one-third">
            <b-input
            placeholder="Core Name"
            v-model="coreNameSearch"
            ></b-input>
          </div>
          <div class="column is-one-third">
            <b-input
            placeholder="Location"
            v-model="locationSearch"
            ></b-input>
          </div>
        </div>

        <div class="columns is-mobile is-centered">
          <div class="column is-two-thirds">
            <b-field grouped>
              <b-input
                placeholder="Parameters, Isotopes, or Researchers..."
                v-model="paramSearch"
                expanded>
              </b-input>
              <p class="control">
                <button class="button is-primary">Search</button>
              </p>
            </b-field>
          </div>
        </div>
      </form>

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
            <div>
              <span
              v-for="(param, idx) in props.row.parameters.slice(0, maxDisplayParams)"
              :key="idx"
              >
                {{
                  format(
                    idx,
                    Math.min(props.row.parameters.length, maxDisplayParams),
                    param.type
                  )
                }}
              </span>
            </div>
            </b-table-column>

            <b-table-column centered v-slot="props">
              <b-button
              type="is-primary"
              @click.prevent="downloadFile(`${props.row.document_file}`)"
              icon-left="file-download"
              outlined
              download>
                Download
              </b-button>
            </b-table-column>

            <template slot="detail" slot-scope="props">
              <article class="media">
                <div class="media-content">
                  <div class="content">
                    <p>
                      Researchers:
                      <ul>
                        <li
                        v-for="(researcher, idx) in props.row.researchers" 
                        :key="idx"
                        >
                          {{ researcher.first_name }} {{ researcher.last_name }}
                        </li>
                      </ul>
                      Isotopes:
                      <ul>
                        <li
                        v-for="(isotope, idx) in props.row.isotopes"
                        :key="idx"
                        >
                          {{ isotope.name }} {{ isotope.symbol }}
                        </li>
                      </ul>
                      Parameters:
                      <ul>
                        <li
                        v-for="(param, idx) in props.row.parameters"
                        :key="idx"
                        >
                          {{ param.type }}
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
      maxDisplayParams: 3,
      coreNameSearch: '',
      locationSearch: '',
      paramSearch: ''
    };
  },

  methods: {
    loadAsyncData() {
      const params = [
        `limit=${this.perPage}`,
        `offset=${this.page - 1}`,
        `search=${this.searchParams}`
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

    onSearch() {
      this.searchParams = [
        this.coreNameSearch,
        this.locationSearch,
        this.paramSearch
        ].join(',');
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

    format(idx, maxIdx, paramType) {
      return idx !== (maxIdx - 1) ? `${paramType},` : paramType;
   }
  },

  mounted() {
    this.loadAsyncData();
  },
}
</script>