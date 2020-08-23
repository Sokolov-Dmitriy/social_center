<template>
  <div>
    <nav-bar></nav-bar>
    <ClientsList></ClientsList>
  </div>
</template>

<script>
  // import ClientsList from '@/componets/ClientsList'
  import ClientsList from "./ClientsList";
  import navBar from "./navBar";


  export default {
    name: 'MainWindow',
    components: {
      ClientsList,
      navBar
    },

    methods: {

      login() {
        this.$router.push({name: 'login'})
      }

    }
  }
</script>

<style scoped>

</style>
