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
    <next-back v-bind:url="'childAdd'"></next-back>
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
  </div>
</template>

<script>
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import sideBarTest from "../Test/sideBarTest";
import NextBack from "./NextBack";

export default {
  name: "ChildAdd",
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
      this.items['age'] = (
        dateNow.getFullYear() < date.getFullYear()
      ) ? -1 : (
        (dateNow.getMonth() < date.getMonth()
        ) ? -1 : (
          (dateNow.getDate() < date.getDate()
          ) ? -1 :
            Math.abs(ageDate.getUTCFullYear() - 1970))
      );
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
