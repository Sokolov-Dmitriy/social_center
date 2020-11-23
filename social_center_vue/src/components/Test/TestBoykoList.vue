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
      <next-back v-bind:url="'testBoykoList'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Модифицированная шкала социального функционирования при синдроме зависимости (Бойко
          Е.О.)
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
                type="button" @click="toGraphic">Сравнение результатов <span
          class="fa fa-bar-chart-o fa-2x"></span></button>
      </div>
    </div>
    <MainFooter v-if="tests" class="noprint"></MainFooter>
  </div>
</template>

<script>
import navBar from "../navBars/navBar";
import sideBar from "../sideBar";
import sideBarTest from "./sideBarTest";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "TestBoykoList",
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
      url: this.$store.state.baseUrl + "api/testBoykoList/",
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
        this.$router.push({name: 'testBoyko', params: {id: id, attempt: attempt}});
    },
    toAddTest(attempt) {
      this.$router.push({name: 'testBoyko', params: {id: 0, attempt: attempt}})
    },
    toGraphic() {
      this.$router.push({name: 'graphicBoyko'})
    }
  }
}
</script>

<style scoped>
.general {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.container {
  margin-top: 2%;
  text-align: center;
  flex: 1;
}

.my-link {
  background-color: #FFF8DC;
  color: #492727;
  font-size: 20px;
  margin-left: 20px;
}

.btn-default:hover {
  background-color: #E6DFC6;
  color: black;
}

.btn-default {
  color: #492727;
  font-size: 16px;
}

.btn-graphic {
  color: #492727;
  font-size: 18px;
}

.btn-graphic:hover {
  background-color: #E6DFC6;
  color: black;
}

.btn-default-right {
  float: right;
  color: #492727;
  font-size: 16px;
}

.btn-default-right:hover {
  background-color: #E6DFC6;
  color: black;
}

.card-header {
  display: block;
  font-size: 30px;
  font-weight: 700;
  padding: 30px 0;
  /*margin-bottom: 20px;*/
  color: #492727;
  background-color: #D2B48C;
  /*border-color: #D2B48C*/
}

.card {
  background-color: #f5eed5;
  /*margin-bottom: 5%;*/
}

.thead {
  background-color: #D2B48C;
  color: #492727;
}

.tbody {
  color: #492727;
  text-align: center;
  border-color: #f5eed5;
}

.table td, .table th {
  border-color: #f5eed5;
}

.btn-add {
  margin-top: 6px;
  background-color: #D2B48C;
  color: #492727;
  border-color: #D2B48C;
}

.btn-add:hover {
  margin-top: 6px;
  background-color: #492727;
  color: #D2B48C;
  border-color: #492727;
}

@media print {
  .noprint {
    display: none;
  }
}

@media only screen and (max-width: 768px) {
  .my-link {
    font-size: 16px;
    margin-left: 0;
  }
}

@media only screen and (max-width: 650px) {
  .my-link {
    font-size: 14px;
    margin-left: 0;
  }
}

@media only screen and (max-width: 540px) {
  .my-link {
    font-size: 12px;
    margin-left: 0;
  }
}
</style>
