<template>
  <div>
  <selection-menu v-show="showSelection" v-on:get-list="getList"></selection-menu>
  <sub-menu v-bind:matrix="matrix"
            v-bind:markingArray="markingArray"
            v-show="showSubMenu"></sub-menu>
  </div>
</template>

<script>
  import SelectionMenu from "./SelectionMenu";
  import SubMenu from "./SubMenu";
  import $ from "jquery";

  export default {
    name: "MainPageComp",
    data() {
      return {
        showSelection: true,
        showSubMenu:false,
        matrix:{
          labels:[],
          lines:[]
        },
        markingArray:[]


      }
    },
    components: {
      SelectionMenu,
      SubMenu,

    },
    methods: {
      getList(list) {
        console.log(list);
        this.showSelection = !this.showSelection;
        this.showSubMenu = !this.showSubMenu;
        $.ajax({
          url: this.$store.state.baseUrl+"api/" + "get-table" + "/",
          type: "GET",
          data: {
            tables: list
          },
          success: (response) => {
            // console.log(response.data);
            // this.matrix = new Map();
            // this.matrix.set('labels',response.data[0]);
            // this.matrix.set('lines',[]);
            this.matrix.labels=response.data[0];
            this.markingArray=response.data[2];
            // this.markingArray.notFilterMarking=response.data[2];
            for (var key in response.data[1]) {
              // console.log(response.data[1][key] );
              // this.matrix.get('lines').push(response.data[1][key]);
              this.matrix.lines.push(response.data[1][key]);
              // console.log("key:"+key);
            }

            console.log(response.data[2]);
            // this.markingArray=response.data[2];
            // this.notFilterMarkingArray=response.data[2];
            // for(let value in this.markingArray){
            //   console.log(value)
            // }
            // console.log(this.markingArray);

          }
        })
      }
    }
  }
</script>

<style scoped>

</style>



