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
      <next-back v-bind:url="'childAdd'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление ребенка</div>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
            <div class="my-block">2.1 Общая информация</div>
            <div v-for="(value,key) in labels" :key="key">
              <div v-if="key==='health'" class="my-block">2.2 Информация о состоянии здоровья ребёнка</div>
              <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right"
                            class="my-form-group">
                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-if="choices[key]">
                  <b-form-select :options="choices[key]" v-model="items[key]"
                                 :state="getValidationState(validationContext)">
                    <template v-slot:first>
                      <b-form-select-option :value="null"></b-form-select-option>
                    </template>
                  </b-form-select>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="['DateOfCreationIPSO','ContractPeriod'].includes(key)">
                  <b-form-input v-model="items[key]" :state="getValidationState(validationContext)" type="date"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="key==='birthdate'">
                  <b-form-input v-model="items[key]"
                                :state="getValidationState(validationContext)" type="date"
                                @change="getAge(items[key])"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="key==='age'">
                  <b-form-input v-model="items[key]"
                                :state="getValidationState(validationContext)" type="number" min="0"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else>
                  <b-form-input v-model="items[key]"
                                :state="getValidationState(validationContext)" type="text"/>
                </validation-provider>

              </b-form-group>
            </div>
            <button class="btn btn-default" type="reset">Отмена</button>
            <button class="btn btn-default" type="submit">Добавить</button>

          </b-form>
        </validation-observer>
      </div>
    </div>
    <MainFooter v-if="choices"></MainFooter>
  </div>
</template>

<script>
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import sideBarTest from "../Test/sideBarTest";
import NextBack from "./NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "ChildAdd",
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
      // id: '',
      items: '',
      labels: '',
      choices: '',
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/fields/",
      type: "GET",
      data: {model: 'Child'},
      success: (response) => {
        this.labels = response.data.labels;
        this.choices = response.data.choices;
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
        url: this.$store.state.baseUrl + "api/child/",
        type: "POST",
        data: this.items,
        context: this,
        success: (response) => {
          // alert("Данные добавлены.");
          this.$router.push({name: 'childList'})
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
        }
      });
    },
    notSave() {
      this.$router.push({name: 'childList'})
    },
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
    getAge(dod) {
      var date = new Date(dod);
      var ageDifMs = Date.now() - date.getTime();
      var ageDate = new Date(ageDifMs);
      var dateNow = new Date(Date.now());
      // this.items['age'] = (dateNow.getDate() < date.getDate() ||
      //   dateNow.getMonth() < date.getMonth() ||
      //   dateNow.getFullYear() < date.getFullYear()) ?
      //   -1 : Math.abs(ageDate.getUTCFullYear() - 1970);
      // this.items['age'] = (
      //   dateNow.getFullYear() < date.getFullYear()
      // ) ? -1 : (
      //   (dateNow.getMonth() < date.getMonth()
      //   ) ? -1 : (
      //     (dateNow.getDate() < date.getDate()
      //     ) ? -1 :
      //       Math.abs(ageDate.getUTCFullYear() - 1970))
      // );
      if (dateNow.getFullYear() > date.getFullYear()) {
        this.items['age'] = Math.abs(ageDate.getUTCFullYear() - 1970);
      } else {
        if (dateNow.getFullYear() < date.getFullYear()) {
          this.items['age'] = -1;
        } else {
          if (dateNow.getMonth() > date.getMonth()) {
            this.items['age'] = Math.abs(ageDate.getUTCFullYear() - 1970);
          } else {
            if (dateNow.getMonth() < date.getMonth()) {
              this.items['age'] = -1;
            } else {
              if (dateNow.getDate() >= date.getDate()) {
                this.items['age'] = Math.abs(ageDate.getUTCFullYear() - 1970);
              } else {
                this.items['age'] = -1;
              }
            }
          }
        }
      }
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/add-style.css";
</style>
