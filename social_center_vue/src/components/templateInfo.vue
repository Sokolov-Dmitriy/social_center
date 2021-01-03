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
        <div class="card-header" v-html="header"></div>
        <div v-if="url!=='expertOpinion'" class="my-block">{{ subtitle }}</div>
        <table class="table table-hover" v-if="!isHide">
          <!--          <thead class="thead noprint">-->
          <!--          <tr>-->
          <!--            <th scope="col"><br></th>-->
          <!--            <th scope="col"><br></th>-->
          <!--          </tr>-->
          <!--          </thead>-->
          <tbody v-for="(value,key) in labels" class="tbody">
          <tr v-if="!['id','client','child','husband','specialist','family_member'].includes(key) ">
            <td class="td-left">{{ labels[key] }}</td>
            <td>{{ items[key] }}</td>
          </tr>
          </tbody>
        </table>
        <!--        <button class="btn btn-default" type="button" v-if="no_data && !isHide" @click="addInfo">ДОБАВИТЬ <span-->
        <!--          class="fa fa-plus-circle fa-2x"/></button>-->
      </div>
    </div>
  </div>
</template>

<script>
import sideBar from "./sideBar";
import navBar from "./navBars/navBar";
import sideBarTest from "./Test/sideBarTest";
import templateChild from "./Information/templateChild";
import NextBack from "./Information/NextBack";

export default {
  name: "templateInfo",
  components: {
    NextBack,
    sideBar,
    navBar,
    sideBarTest,
    templateChild
  },
  props: {
    url: '',
    header: '',
    subtitle: '',
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
      this.labels = '';
    },
    getRequest() {
      var map = {};
      map[this.identifier_field] = this.identifier;
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/',
        type: "GET",
        data: map,
        success: (response) => {
          if (response === undefined) {
            this.no_data = true;
            this.addInfo();
          } else {
            this.id = response.data[0].id;
            this.items = response.data[0].attributes;
            this.labels = response.data[0].attributes.labels;
            if (this.url === 'child') this.$refs.templateChild.slice(this.items, this.labels);
            if (this.url === 'client') this.$store.commit('storeName', this.items.full_name);
          }
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
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
          // this.$emit('postInfo');
          if (!['client', 'child', 'husbandInformation'].includes(this.url))
            this.addInfo();
          if (this.url === 'client') this.$router.push({name: 'mainwindow'});
          else if (this.url === 'child') this.$router.push({name: 'childList'});
          else if (this.url === 'husbandInformation') this.$router.push({name: 'husbandList'});
          else if (this.url === 'anotherFamilyMembers') this.$router.push({name: 'anotherMembersList'});
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
@import "../assets/css/view-style.css";
</style>
