<template>
  <div>
    <nav-bar></nav-bar>
    <ClientsList></ClientsList>
    <MainFooter></MainFooter>
  </div>
</template>

<script>
  import ClientsList from "./ClientsList";
  import navBar from "../navBars/navBar";
  import MainFooter from "../footers/MainFooter";

  export default {
    name: 'MainWindow',
    components: {
      MainFooter,
      ClientsList,
      navBar
    }
  }
</script>

<style scoped>

</style>
