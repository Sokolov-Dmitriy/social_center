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
      <next-back v-bind:url="'typologicalGroupList'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Типологические группы</div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Диагностика</th>
            <th scope="col">Статус</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="group in groups" @click="toGroup(group.id,group.value)">
            <td>{{ group.name }}</td>
            <td v-if="group.status==='Добавлен'">{{ group.status }}</td>
            <b-button v-else class="btn btn-add" @click="toAddGroup(group.value)">Добавить <span
              class="fa fa-plus-circle"></span></b-button>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <MainFooter v-if="groups" class="noprint"></MainFooter>
  </div>
</template>

<script>
import sideBarTest from "./sideBarTest";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "TypologicalGroupList",
  components: {
    NextBack,
    sideBarTest,
    sideBar,
    navBar,
    MainFooter
  },
  data() {
    return {
      groups: {
        first: {
          value: 1,
          name: 'Первичная',
          id: '',
          status: 'Не добавлен',
        },
        second: {
          value: 2,
          name: 'Вторичная',
          id: '',
          status: 'Не добавлен',
        }
      },
      items: ''
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/typologicalGroupList/",
      type: "GET",
      data: {client: sessionStorage.getItem("id")},
      success: (response) => {
        this.items = response.data.data;
        // console.log(this.items)
        for (let item in this.items) {
          if (this.items[item].test.attempt === 1) {
            this.groups.first.status = 'Добавлен';
            this.groups.first.id = this.items[item].id;
          } else if (this.items[item].test.attempt === 2) {
            this.groups.second.status = 'Добавлен';
            this.groups.second.id = this.items[item].id;
          }
        }
      },
      error: (response) => {
        if (response.status === 401) this.logOut();
        else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
      }
    });
  },
  methods: {
    toGroup(id, attempt) {
      if (id !== '')
        this.$router.push({name: 'typologicalGroup', params: {id: id, attempt: attempt}});
    },
    toAddGroup(attempt) {
      this.$router.push({name: 'typologicalGroup', params: {id: 0, attempt: attempt}})
    },
  }
}
</script>

<style scoped>
@import "../../assets/css/list-style.css";
</style>
