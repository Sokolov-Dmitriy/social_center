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
      <next-back v-bind:url="'husbandAdd'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление партнёра (мужа/жены)</div>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
            <div v-for="(value,key) in labels" :key="key">
              <div v-if="'registrationAddressCity'===key" class="my-little-block">Адрес регистрации</div>
              <div v-if="'actualAddressCity'===key" class="my-little-block">Адрес фактического проживания</div>
              <div v-if="'telephoneNumber'===key" class="my-little-block"></div>
              <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right" class="my-form-group">

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-if="choices[key]">
                  <b-form-select :value="items[key]" :options="choices[key]" v-model="items[key]"
                                 :state="getValidationState(validationContext)">
                    <template v-slot:first>
                      <b-form-select-option :value="null"></b-form-select-option>
                    </template>
                  </b-form-select>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="['aboutWork','aboutNoWork','kindOfDrug'].includes(key)">
                  <b-textarea v-model="items[key]" :value="items[key]" :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider :rules="{required: false,length:6}" v-slot="validationContext"
                                     v-else-if="['registrationAddressIndex','actualAddressIndex'].includes(key)">
                  <b-form-input v-model="items[key]" :value="items[key]" type="number"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider
                  :rules="{required: false,regex:/^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/ }"
                  v-slot="validationContext"
                  v-else-if="key === 'telephoneNumber'">
                  <b-form-input type="tel" v-model="items[key]" :value="items[key]"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="['DateOfCreationIPSO','ContractPeriod'].includes(key)">
                  <b-form-input type="date" v-model="items[key]" :value="items[key]"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="key === 'dod'">
                  <b-form-input type="date" v-model="items[key]" :value="items[key]"
                                :state="getValidationState(validationContext)" @change="getAge(items[key])"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="key === 'age'">
                  <b-form-input type="number" v-model="items[key]" :value="items[key]" min="0"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext"
                                     v-else-if="['durationOfUse','durationOfRemissionD','durationOfRemissionA'].includes(key)">
                  <b-form-input type="number" v-model="items[key]" :value="items[key]" step="0.5" min="0.0" max="99.0"
                                :state="getValidationState(validationContext)"/>
                </validation-provider>

                <validation-provider :rules="{required: false}" v-slot="validationContext" v-else>
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
    <MainFooter v-if="choices"></MainFooter>
  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import sideBarTest from "../Test/sideBarTest";
import MainFooter from "../footers/MainFooter";

export default {
  name: "HusbandAdd",
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
      choices: '',
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/fields/",
      type: "GET",
      data: {model: 'HusbandInformation'},
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
        url: this.$store.state.baseUrl + "api/husbandInformation/",
        type: "POST",
        data: this.items,
        context: this,
        success: (response) => {
          this.$router.push({name: 'husbandList'})
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
        }
      });
    },
    notSave() {
      this.$router.push({name: 'husbandList'})
    },
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
    getAge(dod) {
      var date = new Date(dod);
      var ageDifMs = Date.now() - date.getTime();
      var ageDate = new Date(ageDifMs);
      var dateNow = new Date(Date.now());
      // var age = Math.abs(ageDate.getUTCFullYear() - 1970);
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
      // this.items['age'] = (dateNow.getDate() < date.getDate() ||
      //   dateNow.getMonth() < date.getMonth() ||
      //   dateNow.getFullYear() < date.getFullYear()) ?
      //   -1 : Math.abs(ageDate.getUTCFullYear() - 1970);
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/add-style.css";

.my-little-block {
  text-align: center;
  color: #492727;
  font-size: 16px;
  padding: 2%;
}
</style>
