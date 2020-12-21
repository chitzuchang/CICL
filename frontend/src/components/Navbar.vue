<template>
  <section class="hero is-primary">
    <div class="hero-head">
      <nav class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <div class="navbar-item">
              <img src="../assets/cicl_logo.png" alt="CICL Logo" />
            </div>
            <div class="navbar-item">
              <h1 class="title">Canadian Ice Core Lab</h1>
            </div>
          </div>
          <div class="navbar-menu">
            <div class="navbar-end">
              <span class="navbar-item">
                <b-button type="is-info" @click="redirect" inverted outlined>
                  Admin
                </b-button>
              </span>
            </div>
          </div>
        </div>
      </nav>
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
