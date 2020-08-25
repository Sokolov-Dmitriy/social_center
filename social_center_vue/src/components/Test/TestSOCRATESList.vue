<template>
  <div>
    <div class="noprint">
      <nav-bar></nav-bar>
      <button class="btn btn-default" type="button" v-b-toggle.sidebar-border>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <b-link to="/info" class="my-link">Общие сведения</b-link>
      <button class="btn btn-default-right" type="button" v-b-toggle.sidebar-test>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <side-bar-test></side-bar-test>
      <side-bar></side-bar>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Методика SOCRATES</div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Диагностика</th>
            <th scope="col">Статус</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="test in tests" @click="toTest(test.id,test.value)">
            <td>{{test.name}}</td>
            <td>{{test.status}}</td>
          </tr>
          </tbody>
        </table>
        <button v-if="tests.first.status==='Добавлен' && tests.second.status==='Добавлен'" class="btn btn-graphic noprint"
                type="button" @click="toGraphic">Сравнение результатов <span class="fa fa-bar-chart-o fa-2x"></span></button>
      </div>
    </div>
  </div>
</template>

<script>
  import sideBarTest from "./sideBarTest";
  import sideBar from "../sideBar";
  import navBar from "../navBar";

  export default {
    name: "TestSOCRATESList",
    components: {
      sideBarTest,
      sideBar,
      navBar
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
        url: this.$store.state.baseUrl + "api/testSOCRATESList/",
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
          this.$router.push({name: 'testSOCRATES', params: {id: id, attempt: attempt}});
        else this.$router.push({name: 'testSOCRATES', params: {id: 0, attempt: attempt}})
      },
      toGraphic() {
        this.$router.push({name: 'graphicSOCRATES'})
      }
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 2%;
    text-align: center;
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
    color: #492727;
    background-color: #D2B48C;
    /*border-color: #D2B48C*/
  }

  .card {
    background-color: #f5eed5;
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

  @media print {
    .noprint {
      display: none;
    }
  }
</style>
