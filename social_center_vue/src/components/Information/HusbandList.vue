<template>
  <div class="general">
    <div class="noprint">
      <nav-bar></nav-bar>
      <button class="btn btn-default" type="button" v-b-toggle.sidebar-border>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <b-link to="/info" class="my-link">{{ this.$store.state.fullName }}</b-link>
      <button class="btn btn-default-right" type="button" v-b-toggle.sidebar-test>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <side-bar-test></side-bar-test>
      <side-bar></side-bar>
      <next-back v-bind:url="'husbandList'"></next-back>
    </div>

    <div class="container">
      <div class="card">
        <div class="card-header">Сведения о партнёре (муже/жене)</div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">ФИО</th>
            <th scope="col">Возраст</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="husband in husbands" @click="toInfo(husband.id)">
            <td>{{ husband.attributes.fullName }}</td>
            <td>{{ husband.attributes.age }}</td>
          </tr>
          </tbody>
        </table>
        <button class="btn btn-default noprint" type="button" @click="addHusband">ДОБАВИТЬ ПАРТНЕРА (МУЖА/ЖЕНУ) <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>
    <MainFooter v-if="husbands" class="noprint"></MainFooter>
  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import sideBarTest from "../Test/sideBarTest";
import MainFooter from "../footers/MainFooter";

export default {
  name: "HusbandList",
  components: {
    NextBack,
    sideBar,
    navBar,
    sideBarTest,
    MainFooter
  },
  data() {
    return {
      husbands: ''
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/husbands/",
      type: "GET",
      data: {client: sessionStorage.getItem("id")},
      success: (response) => {
        this.husbands = response.data
      },
      error: (response) => {
        if (response.status === 401) this.logOut();
        else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
      }
    });
  },
  methods: {
    addHusband() {
      ////////////////////////////////
      /////////////////////////////
      ////////ВРЕМЕННООООООООО1
      /////////////////////////////////
      if (this.husbands.length >= 1) {
        alert("По техническим причинам в данные момент нельзя добавить более одного партнера. \nВ ближайшее время проблема будет решена.")
      } else {
        this.$router.push({name: 'husbandAdd'})
      }
    },
    toInfo(value) {
      this.$router.push({name: 'husbandInformation', params: {id: value}})
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/list-style.css";

@media print {
  .tbody {
    page-break-after: auto;
    page-break-inside: avoid;
    border: none !important;
    margin-bottom: 20px !important;
  }
}

</style>
