<template>
  <div>
    <b-sidebar id="sidebar-test" title="Тесты" header-class="my-header" body-class="my-body"
               backdrop right>
      <b-list-group>
        <b-list-group-item class="my-title-one" to="/testBoykoList">Модифицированная шкала социального функционирования при синдроме
          зависимости (Бойко Е.О.)
        </b-list-group-item>
        <b-list-group-item class="my-title-one" to="/testGAGEList">Модифицированная методика определения степени вовлечённости в
          потребление ПАВ (GAGE)
        </b-list-group-item>
        <b-list-group-item class="my-title-one" to="/testSOCRATESList">SOCRATES</b-list-group-item>
        <b-list-group-item class="my-title-one" to="/typologicalGroupList">Типологические группы</b-list-group-item>
      </b-list-group>
    </b-sidebar>
  </div>
</template>

<script>
  export default {
    name: "sideBarTest"
  }
</script>

<style scoped>
  /deep/ .my-header {
    background-color: #D2B48C;
    color: #492727;
  }

  /deep/ .my-body {
    background-color: #FFF8DC;
  }

  .my-title-one:hover {
    background-color: #EEE7CE;
    color: black;
  }

  .my-title-one {
    font-size: 16px;
    color: #492727;
    background-color: #FFF8DC;
    padding: 30px;
    /*text-align: center;*/
  }
</style>
