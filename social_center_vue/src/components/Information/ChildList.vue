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
      <next-back v-bind:url="'childList'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">2. Сведения о детях</div>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">ФИО</th>
            <th scope="col">Пол</th>
            <th scope="col">Возраст</th>
          </tr>
          </thead>
          <tbody class="tbody">
          <tr v-for="child in children" @click="toInfo(child.id)">
            <td>{{child.attributes.full_name}}</td>
            <td>{{child.attributes.sex}}</td>
            <td>{{child.attributes.age}}</td>
          </tr>
          </tbody>
        </table>
        <button class="btn btn-default noprint" type="button" @click="addChild">ДОБАВИТЬ РЕБЕНКА <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>

  </div>
</template>

<script>
  import navBar from "../navBars/navBar";
  import sideBar from "../sideBar";
  import sideBarTest from "../Test/sideBarTest";
  import NextBack from "./NextBack";

  export default {
    name: "ChildList",
    components: {
      NextBack,
      sideBar,
      navBar,
      sideBarTest
    },
    data() {
      return {
        children: ''
      }
    },
    created() {
      $.ajax({
        url: this.$store.state.baseUrl+"api/children/",
        type: "GET",
        data: {client: sessionStorage.getItem("id")},
        success: (response) => {
          this.children = response.data
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    },
    methods: {
      addChild() {
        this.$router.push({name: 'childAdd'})
      },
      toInfo(value) {
        this.$router.push({name: 'child', params: {id: value}})
      }
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 2%;
    text-align: center;
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

  .my-link {
    background-color: #FFF8DC;
    color: #492727;
    font-size: 20px;
    margin-left: 20px;
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

  /*td .btn{*/
  /*  background-color: #D2B48C;*/
  /*  color: #492727;*/
  /*  border-color: #D2B48C;*/
  /*}*/
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
    @media print {
    .noprint {
      display: none;
    }

    .tbody {
      page-break-after: auto;
      page-break-inside: avoid;
      border: none !important;
      margin-bottom: 20px !important;
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
