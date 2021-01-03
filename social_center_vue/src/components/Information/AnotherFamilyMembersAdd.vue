<template>
  <div class="general">
    <div class="header">
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
      <next-back v-bind:url="'anotherFamilyMembersAdd'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление члена семьи</div>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
            <div v-for="(value,key) in labels" :key="key">
              <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right" class="my-form-group">

                <validation-provider :rules="{required: false}" v-slot="validationContext">
                  <b-form-input type="text" v-model="items[key]" :value="items[key]"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

              </b-form-group>
            </div>
            <button class="btn btn-default" type="reset">Отмена</button>
            <button class="btn btn-default" type="submit">Добавить</button>
          </b-form>
        </validation-observer>
      </div>
    </div>
    <MainFooter v-if="labels"></MainFooter>
  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import {ValidationObserver, ValidationProvider} from "vee-validate";
import sideBarTest from "../Test/sideBarTest";
import MainFooter from "../footers/MainFooter";

export default {
  name: "AnotherFamilyMembersAdd",
  components: {
    NextBack,
    sideBar,
    navBar,
    ValidationProvider,
    ValidationObserver,
    sideBarTest,
    MainFooter,
  },
  data() {
    return {
      items: '',
      labels: '',
      // choices: '',
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/fields/",
      type: "GET",
      data: {model: 'AnotherFamilyMembers'},
      success: (response) => {
        this.labels = response.data.labels;
        // this.choices = response.data.choices;
        this.items = response.data.items;
      },
      error: (response) => {
        if (response.status === 401) this.logOut();
        else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
      }
    })
  },
  mounted: function () {
    this.templateBool = true
  },
  methods: {
    save() {
      this.items['client'] = parseInt(sessionStorage.getItem('id'));
      $.ajax({
        url: this.$store.state.baseUrl + "api/anotherFamilyMembers/",
        type: "POST",
        data: this.items,
        context: this,
        success: (response) => {
          this.$router.push({name: 'anotherMembersList'})
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
        }
      });
    },
    notSave() {
      this.$router.push({name: 'anotherMembersList'})
    },
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
  }
}
</script>

<style scoped>
@import "../../assets/css/add-style.css";
</style>
