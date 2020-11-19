<template>
  <div>
    <Navbar />
    <SearchTable />
    <Footer />
  </div>
</template>

<script>
  import Navbar from "./components/Navbar";
  import SearchTable from "./components/SearchTable";
  import Footer from "./components/Footer";

  export default {
    name: "App",
    components: {
      Navbar,
      SearchTable,
      Footer,
    },
  };
</script>
