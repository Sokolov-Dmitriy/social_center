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
            <td>{{group.status}}</td>
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
  import navBar from "../navBar";
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
        else this.$router.push({name: 'typologicalGroup', params: {id: 0, attempt: attempt}})
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
