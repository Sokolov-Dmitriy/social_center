<template>
  <div>
    <b-sidebar id="sidebar-border" title="Социальная диагностика" header-class="my-header" body-class="my-body"
               backdrop>
      <b-list-group>
        <b-list-group-item class="my-big-list-group-item">
          <header class="my-title">1. Сведения о клиенте</header>
          <b-list-group class="my-link-group">
            <b-list-group-item class="my-link" to="/info">1.1 Общая информация</b-list-group-item>
            <b-list-group-item class="my-link" to="/socialBehavior">1.2 Информация о противоправных действиях,
              правонарушениях,
              употреблении наркотиков, алкоголя
            </b-list-group-item>
            <b-list-group-item class="my-link" to="/chronicDisease">1.3 Информация о наличии хронического заболевания
            </b-list-group-item>
          </b-list-group>
        </b-list-group-item>
        <b-list-group-item class="my-title-one" to="/childList">2. Сведения о детях</b-list-group-item>
        <b-list-group-item class="my-title-one" to="/familyMembers">3. Сведения о членах семьи</b-list-group-item>
        <b-list-group-item class="my-big-list-group-item">
          <header class="my-title">4. Сведения о социально-бытовом и социально-экономическом положении</header>
          <b-list-group class="my-link-group">
            <b-list-group-item class="my-link" to="/socialLiving">4.1 Социально-бытовые условия</b-list-group-item>
            <b-list-group-item class="my-link" to="/socialEconomic">4.2 Социально-экономические условия проживания
            </b-list-group-item>
          </b-list-group>
        </b-list-group-item>
        <b-list-group-item class="my-title-one margin" to="/expertOpinion">5. Заключение специалиста</b-list-group-item>
      </b-list-group>
    </b-sidebar>
  </div>
</template>

<script>
  export default {
    name: "sideBar"
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

  .my-link-group {
    margin-top: 2%;
  }

  .my-link {
    background-color: #FFF8DC;
    color: #492727;
    font-size: 14px;
  }

  .my-link:hover {
    background-color: #EEE7CE;
    color: black;
  }

  .my-title-one:hover {
    background-color: #EEE7CE;
    color: black;
  }

  .my-title-one {
    font-size: 16px;
    color: #492727;
    background-color: #FFF8DC;
  }

  .my-title {
    font-size: 16px;
    color: #492727;
    background-color: #FFF8DC;
  }

  .my-big-list-group-item {
    background-color: #FFF8DC;
  }

  .margin {
    margin-bottom: 75px;
  }
</style>
