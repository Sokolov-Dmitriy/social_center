<template>
  <div class="general">
    <nav-bar></nav-bar>
    <ClientsList class="list"></ClientsList>
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
/*.list {*/
/*  margin-top: 80px;*/
/*}*/

.general {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.list {
  flex: 1;
}
</style>
