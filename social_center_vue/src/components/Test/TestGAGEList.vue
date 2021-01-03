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
      <next-back v-bind:url="'testGAGEList'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Модифицированная методика определения степени вовлечённости в потребление ПАВ (GAGE)
        </div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Диагностика</th>
            <th scope="col">Статус</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="test in tests" @click="toTest(test.id,test.value)">
            <td>{{ test.name }}</td>
            <td v-if="test.status==='Добавлен'">{{ test.status }}</td>
            <b-button v-else class="btn btn-add" @click="toAddTest(test.value)">Добавить <span
              class="fa fa-plus-circle"></span></b-button>
          </tr>
          </tbody>
        </table>
        <button v-if="tests.first.status==='Добавлен' && tests.second.status==='Добавлен'"
                class="btn btn-graphic noprint"
                type="button" @click="toGraphic">Сравнение результатов <span class="fa fa-bar-chart-o fa-2x"></span>
        </button>
      </div>
    </div>
    <MainFooter v-if="tests" class="noprint"></MainFooter>
  </div>
</template>

<script>
import sideBarTest from "./sideBarTest";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "TestGAGEList",
  components: {
    NextBack,
    sideBarTest,
    sideBar,
    navBar,
    MainFooter
  },
  data() {
    return {
      tests: {
        first: {
          value: 1,
          name: 'Первичная',
          id: '',
          status: 'Не добавлен'
        },
        second: {
          value: 2,
          name: 'Вторичная',
          id: '',
          status: 'Не добавлен'
        }
      },
      items: ''
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/testGAGEList/",
      type: "GET",
      data: {client: sessionStorage.getItem("id")},
      success: (response) => {
        this.items = response.data;
        for (let test in this.items) {
          if (this.items[test].attributes.attempt === 1) {
            this.tests.first.status = 'Добавлен';
            this.tests.first.id = this.items[test].id;
          } else if (this.items[test].attributes.attempt === 2) {
            this.tests.second.status = 'Добавлен';
            this.tests.second.id = this.items[test].id;
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
    toTest(id, attempt) {
      if (id !== '')
        this.$router.push({name: 'testGAGE', params: {id: id, attempt: attempt}});
    },
    toAddTest(attempt) {
      this.$router.push({name: 'testGAGE', params: {id: 0, attempt: attempt}})
    },
    toGraphic() {
      this.$router.push({name: 'graphicGAGE'})
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/list-style.css";

.btn-graphic {
  color: #492727;
  font-size: 18px;
}

.btn-graphic:hover {
  background-color: #E6DFC6;
  color: black;
}
</style>
