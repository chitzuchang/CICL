<template>
  <section class="hero is-info is-bold">
    <div class="hero-head">
      <div class="container">
        <div class="columns is-vcentered">
          <div class="column" style="padding: 2%">
            <img src="../assets/cicl_logo.png" alt="CICL Logo" />
          </div>
          <div class="column is-8">
            <h1 class="title">Canadian Ice Core Lab</h1>
          </div>
          <div class="column is-2">
            <b-button type="is-info" @click="redirect" inverted outlined>
              Admin
            </b-button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    redirect() {
      window.location.href = "admin";
    },
  },
};
</script>
