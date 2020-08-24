<template>
  <div>
    <nav-bar class="nav"></nav-bar>
    <selection-menu v-show="showSelection" v-on:get-list="getList"></selection-menu>
    <sub-menu class="sub-menu" v-bind:matrix="matrix"
              v-bind:markingArray="markingArray"
              v-show="showSubMenu"></sub-menu>
  </div>
</template>

<script>
  import SelectionMenu from "./SelectionMenu";
  import SubMenu from "./SubMenu";
  import $ from "jquery";
  import navBar from "../navBar";

  export default {
    name: "MainPageComp",
    data() {
      return {
        showSelection: true,
        showSubMenu: false,
        matrix: {
          labels: [],
          lines: []
        },
        markingArray: []


      }
    },
    components: {
      SelectionMenu,
      SubMenu,
      navBar,

    },
    methods: {
      getList(list) {
        console.log(list);
        this.showSelection = !this.showSelection;
        this.showSubMenu = !this.showSubMenu;
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + "get-table" + "/",
          type: "GET",
          data: {
            tables: list
          },
          success: (response) => {
            this.matrix.labels = response.data[0];
            this.markingArray = response.data[2];
            for (var key in response.data[1]) {
              this.matrix.lines.push(response.data[1][key]);
            }

            console.log(response.data[2]);
          }
        })
      }
    }
  }
</script>

<style scoped>
  .nav {
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 999;
  }

  .sub-menu {
    z-index: 1;
  }
</style>



