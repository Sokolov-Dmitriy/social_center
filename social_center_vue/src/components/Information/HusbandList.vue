<template>
  <div>
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
        <div class="card-header">Список мужей/партнеров</div>
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
        <button class="btn btn-default noprint" type="button" @click="addHusband">ДОБАВИТЬ МУЖА/ПАРТНЕРА <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>

  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import sideBarTest from "../Test/sideBarTest";

export default {
  name: "HusbandList",
  components: {
    NextBack,
    sideBar,
    navBar,
    sideBarTest
  },
  data() {
    return {
      husbands: ''
    }
  },
  created() {
    if (this.$route.params.id !== undefined)
      sessionStorage.setItem('id_husband', this.$route.params.id);
    this.id = sessionStorage.getItem('id_husband');

    $.ajax({
      url: this.$store.state.baseUrl + "api/husbands/",
      type: "GET",
      data: {husband: sessionStorage.getItem("id_husband")},
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
      if(this.husbands.length>=1){
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
