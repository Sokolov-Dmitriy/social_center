<template>
  <div>
    <nav-bar></nav-bar>
    <ClientsList></ClientsList>
  </div>
</template>

<script>
  import ClientsList from "./ClientsList";
  import navBar from "../navBars/navBar";

  export default {
    name: 'MainWindow',
    components: {
      ClientsList,
      navBar
    }
  }
</script>

<style scoped>

</style>
