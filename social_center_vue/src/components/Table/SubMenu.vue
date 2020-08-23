<template>
  <div>
    <div class="d-flex justify-content-start">
      <div class="mt-2 ml-2 mr-1 item" >Таблица</div>
      <div class="mt-2 ml-1 item" >Подсчеты/Графики</div>
    </div>
<!--    {{markingArray}}-->
    <table-comp v-show="showTable"
                v-bind:matrixAll="matrix"
                v-bind:notFilterLines="notFilterLines"
                v-bind:markingArray="markingArray"
                >
    </table-comp>
<!--                v-bind:marking="marking"-->




<!--    <p style="visibility: visible">ttttt{{matrix.get('labels')}}</p>-->
  </div>
</template>

<script>
  import TableComp from "./TableComp";
  export default {
    name: "SubMenu",
    props:['matrix','markingArray'],
    data(){
      return{
        showTable:true,
        notFilterLines:this.matrix.lines,
        // readyFilter:this.markingArray.filterMarking,
        // notFilter:this.markingArray.notFilterMarking
        // matrixAll:{
        //   labels:this.matrix.labels,
        //   lines:this.matrix.lines,
        //   notFilterLines:this.matrix.lines
        // }
      }
    },
    components:{
      TableComp
    }
  }
</script>

<style scoped>
  .item{
    background-color: grey;
    padding: 5px 10px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;

  }
  .item:hover{
    border: 2px solid red;
    /*border-radius: 10px;*/
  }
</style>

