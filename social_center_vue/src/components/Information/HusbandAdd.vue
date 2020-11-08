<template>
  <div>
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
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление партнёра (мужа/жены)</div>
        <validation-observer ref="observer" v-slot="{ handleSubmit }">
          <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
            <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right"
                          v-for="(value,key) in labels" :key="key" class="my-form-group">

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
                <b-form-input type="number" v-model="items[key]" :value="items[key]" min="1"
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
            <button class="btn btn-default" type="reset">Отмена</button>
            <button class="btn btn-default" type="submit">Добавить</button>
          </b-form>
        </validation-observer>
      </div>
    </div>
  </div>
</template>

<script>
import NextBack from "./NextBack";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import sideBarTest from "../Test/sideBarTest";

export default {
  name: "HusbandAdd",
  components: {
    NextBack,
    sideBar,
    navBar,
    ValidationProvider,
    ValidationObserver,
    sideBarTest
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
      this.items['age'] = Math.abs(ageDate.getUTCFullYear() - 1970);
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
  border-color: #D2B48C
}

.card {
  background-color: #f5eed5;
  /*margin-bottom: 5%;*/
}

form .btn-default {
  background-color: #D2B48C;
  color: #492727;
  margin: 10px;
}

form .btn-default:hover {
  background-color: #452424;
  color: #D2B48C;
}

.btn-default:hover {
  background-color: #E6DFC6;
  color: black;
}

.my-form {
  background-color: #f5eed5;
}

.my-form-group {
  color: #492727;
  margin-right: 3%;
}

.my-link {
  background-color: #FFF8DC;
  color: #492727;
  font-size: 20px;
  margin-left: 20px;
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

.my-block {
  text-align: center;
  color: #492727;
  font-size: 18px;
  padding: 3%;
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
