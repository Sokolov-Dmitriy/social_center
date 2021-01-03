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
      <next-back v-bind:url="'anotherMembersList'"></next-back>
    </div>

    <div class="container">
      <div class="card">
        <div class="card-header">Сведения о других членах семьи</div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Кем приходится</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="member in members" @click="toInfo(member.id)">
            <td>{{ member.attributes.who_is }}</td>
          </tr>
          </tbody>
        </table>
        <button class="btn btn-default noprint" type="button" @click="addMember">ДОБАВИТЬ ЧЛЕНА СЕМЬИ <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>
    <MainFooter v-if="members" class="noprint"></MainFooter>
  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import sideBarTest from "../Test/sideBarTest";
import MainFooter from "../footers/MainFooter";

export default {
  name: "AnotherFamilyMembersList",
  components: {
    NextBack,
    sideBar,
    navBar,
    sideBarTest,
    MainFooter
  },
  data() {
    return {
      members: ''
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/anotherMembers/",
      type: "GET",
      data: {client: sessionStorage.getItem("id")},
      success: (response) => {
        this.members = response.data
      },
      error: (response) => {
        if (response.status === 401) this.logOut();
        else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
      }
    });
  },
  methods: {
    addMember() {
        this.$router.push({name: 'anotherFamilyMembersAdd'})
    },
    toInfo(value) {
      this.$router.push({name: 'anotherFamilyMembers', params: {id: value}})
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
