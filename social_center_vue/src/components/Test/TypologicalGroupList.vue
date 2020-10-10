<template>
  <div>
    <div class="noprint">
      <nav-bar></nav-bar>
      <button class="btn btn-default" type="button" v-b-toggle.sidebar-border>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <b-link to="/info" class="my-link">{{this.$store.state.fullName}}</b-link>
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
            <td>{{group.name}}</td>
            <td v-if="group.status==='Добавлен'">{{group.status}}</td>
            <b-button v-else class="btn btn-add" @click="toAddGroup(group.value)">Добавить <span
              class="fa fa-plus-circle"></span></b-button>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import sideBarTest from "./sideBarTest";
  import sideBar from "../sideBar";
  import navBar from "../navBars/navBar";
  import NextBack from "../Information/NextBack";

  export default {
    name: "TypologicalGroupList",
    components: {
      NextBack,
      sideBarTest,
      sideBar,
      navBar
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

  td {
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
