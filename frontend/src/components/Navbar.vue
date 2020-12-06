<template>
  <section class="hero is-info is-bold">
    <div class="hero-head">
      <div class="navbar">
        <div class="container">
          <div class="navbar-brand">
            <div class="columns is-vcentered">
              <div class="column" style="padding-top:20px; padding-bottom:15px">
                <img
                  src="../assets/cicl_logo.png"
                  alt="CICL Logo"
                  width="400"
                />
              </div>
              <div class="column is-10">
                <h1 class="title">Canadian Ice Core Lab</h1>
              </div>
            </div>
          </div>
          <div class="navbar-menu">
            <div class="navbar-end">
              <div class="buttons">
                <a class="a-menu is-size-10 navbar-item">
                  home
                </a>
                <a class="a-menu is-size-10 navbar-item">
                  about
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    name: "Navbar",
  };
</script>
