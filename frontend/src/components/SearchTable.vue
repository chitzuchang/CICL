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
            @page-change="onPageChange"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page"
            backend-sorting
            :default-sort-direction="defaultSortOrder"
            :default-sort="[sortField, sortOrder]"
            @sort="onSort"
          >
            <b-table-column
              field="original_title"
              label="Location"
              v-slot="props"
            >
              {{ props.row.original_title }}
            </b-table-column>

            <b-table-column
              field="vote_count"
              label="Description"
              width="400"
              v-slot="props"
            >
              {{ props.row.vote_count }}
            </b-table-column>

            <b-table-column label="Download Link" width="400" v-slot="props">
              <button @click="download">
                <i class="far fa-arrow-alt-circle-down" />
              </button>
              {{ props.row.overview | truncate(80) }}
            </b-table-column>
          </b-table>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "SearchTable",
    data: function() {
      return {
        data: [],
        total: 0,
        loading: false,
        sortField: "vote_count",
        sortOrder: "desc",
        defaultSortOrder: "desc",
        page: 1,
        perPage: 20,
      };
    },
    methods: {
      /*
       * Load async data
       */
      loadAsyncData() {
        const params = [
          "api_key=bb6f51bef07465653c3e553d6ab161a8",
          "language=en-US",
          "include_adult=false",
          "include_video=false",
          `sort_by=${this.sortField}.${this.sortOrder}`,
          `page=${this.page}`,
        ].join("&");

        this.loading = true;
        axios
          .get(`https://api.themoviedb.org/3/discover/movie?${params}`)
          .then(({ data }) => {
            // api.themoviedb.org manage max 1000 pages
            this.data = [];
            let currentTotal = data.total_results;
            if (data.total_results / this.perPage > 1000) {
              currentTotal = this.perPage * 1000;
            }
            this.total = currentTotal;
            data.results.forEach((item) => {
              item.release_date = item.release_date
                ? item.release_date.replace(/-/g, "/")
                : null;
              this.data.push(item);
            });
            this.loading = false;
          })
          .catch((error) => {
            this.data = [];
            this.total = 0;
            this.loading = false;
            throw error;
          });
      },
      /*
       * Handle page-change event
       */
      onPageChange(page) {
        this.page = page;
        this.loadAsyncData();
      },
      /*
       * Handle sort event
       */
      onSort(field, order) {
        this.sortField = field;
        this.sortOrder = order;
        this.loadAsyncData();
      },
      /*
       * Type style in relation to the value
       */
      type(value) {
        const number = parseFloat(value);
        if (number < 6) {
          return "is-danger";
        } else if (number >= 6 && number < 8) {
          return "is-warning";
        } else if (number >= 8) {
          return "is-success";
        }
      },
    },
    filters: {
      /**
       * Filter to truncate string, accepts a length parameter
       */
      truncate(value, length) {
        return value.length > length ? value.substr(0, length) + "..." : value;
      },
    },
    mounted() {
      this.loadAsyncData();
    },
  };
</script>
