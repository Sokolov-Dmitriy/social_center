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
      <next-back v-bind:url="url"></next-back>
    </div>


    <div class="container">
      <button class="btn btn-default noprint" type="button" v-if="!no_data" @click="deleteRequest">УДАЛИТЬ <span
        class="fa fa-trash-o fa-2x"/>
      </button>
      <button class="btn btn-default noprint" type="button" v-if="!no_data" @click="addInfo">РЕДАКТИРОВАТЬ <span
        class="fa fa-pencil fa-2x"/>
      </button>
      <template-child v-bind:no_data="no_data" v-bind:is-hide="isHide" ref="templateChild"
                      v-if="url==='child'"></template-child>
      <div class="card" v-if="url!=='child'">
        <div class="card-header" v-if="url==='client' ">{{items.full_name}}</div>
        <div class="card-header" v-else v-html="header"></div>
        <table class="table table-hover" v-if="!isHide">
          <thead class="thead noprint">
          <tr>
            <th scope="col">Поле</th>
            <th scope="col">Значение</th>
          </tr>
          </thead>
          <tbody v-for="(value,key) in labels" class="tbody">
          <tr v-if="!['id','client','child','husband','economic_condition','specialist'].includes(key) ">
            <td>{{labels[key]}}</td>
            <td>{{items[key]}}</td>
          </tr>
          </tbody>
        </table>
        <navigation v-if="!no_data && !isHide" v-bind:url="url" v-bind:id="id" class="noprint"></navigation>
        <button class="btn btn-default" type="button" v-if="no_data && !isHide" @click="addInfo">ДОБАВИТЬ <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>
  </div>
</template>

<script>
  import sideBar from "./sideBar";
  import navBar from "./navBar";
  import navigation from "./Information/navigation";
  import sideBarTest from "./Test/sideBarTest";
  import templateChild from "./Information/templateChild";
  import NextBack from "./Information/NextBack";

  export default {
    name: "templateInfo",
    components: {
      NextBack,
      sideBar,
      navBar,
      navigation,
      sideBarTest,
      templateChild
    },
    props: {
      url: '',
      header: '',
      identifier: '',
      identifier_field: ''
    },
    data() {
      return {
        items: '',
        labels: '',
        no_data: false,
        isHide: false,
        id: '',
        edit: '',
      }
    },
    created() {
      this.getRequest();
    },
    methods: {
      addInfo() {
        this.$emit('addInfo');
        this.isHide = true;
      },
      getRequest() {
        var map = {};
        map[this.identifier_field] = this.identifier;
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + this.url + '/',
          type: "GET",
          data: map,
          success: (response) => {
            if (response === undefined)
              this.no_data = true;
            else {
              this.id = response.data[0].id;
              this.items = response.data[0].attributes;
              this.labels = response.data[0].attributes.labels;
              if (this.url === 'child') this.$refs.templateChild.slice(this.items, this.labels);
            }
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        });
        if (this.url !== "client")
          this.getForPutRequest();
      },
      deleteRequest() {
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.id,
          type: "DELETE",
          success: (response) => {
            this.items = '';
            this.labels = '';
            this.edit = '';
            this.isHide = false;
            this.no_data = true;
            this.$emit('postInfo');
            // alert("Удаление прошло успешно.");
            if (this.url === 'client') this.$router.push({name: 'mainwindow'});
            else if (this.url === 'child') this.$router.push({name: 'childList'});
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        })
      },
      postRequest(items) {
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + this.url + '/',
          type: "POST",
          data: items,
          success: (response) => {
            // alert("Данные добавлены.");
            this.$emit('postInfo');
            this.isHide = false;
            this.no_data = false;
            this.getRequest();
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
          }
        });
      },
      getForPutRequest() {
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.identifier,
          type: "GET",
          success: (response) => {
            if (response !== undefined)
              this.edit = response.data[0].attributes;
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        });
      },
      putRequest(items) {
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.id,
          type: "PUT",
          data: items,
          success: (response) => {
            // alert("Изменение прошло успешно");
            this.$emit('postInfo');
            this.isHide = false;
            this.no_data = false;
            this.getRequest();
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        });
      },
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

  .thead {
    background-color: #D2B48C;
    color: #492727;
  }

  .table {
    /*width: 100%;*/
    table-layout: fixed;
    /*margin: auto;*/
  }

  .tbody {
    color: #492727;
    text-align: center;
    border-color: #f5eed5;
    /*width: 100%;*/
  }

  .btn-default {
    color: #492727;
    font-size: 16px;
  }

  .btn-default:hover {
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

  .my-link {
    background-color: #FFF8DC;
    color: #492727;
    font-size: 20px;
    margin-left: 20px;
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
</style>
