<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление клиента</div>
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
                                   v-else-if="['dateOfInterview','dateOfCertified','dod','passDateIssue'].includes(key)">
                <b-form-input v-model="items[key]" :value="items[key]" type="date"
                              :state="getValidationState(validationContext)"/>
              </validation-provider>

              <validation-provider :rules="{required: false}" v-slot="validationContext"
                                   v-else-if="['passSeries','passNumber','addressIndex','adultsCount','minorsCount'].includes(key)">
                <b-form-input v-model="items[key]" :value="items[key]" type="number" min="0"
                              :state="getValidationState(validationContext)"/>
              </validation-provider>

              <validation-provider :rules="{required: false}" v-slot="validationContext"
                                   v-else-if="key==='age'">
                <b-form-input v-model="items[key]=getAge.toString()" :value="items[key]=getAge.toString()" type="number"
                              :state="getValidationState(validationContext)"/>
              </validation-provider>

              <validation-provider
                :rules="{required: false,regex:/^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/}"
                v-slot="validationContext" v-else-if="key==='phoneNumber'">
                <b-form-input v-model="items[key]" :value="items[key]" type="tel"
                              :state="getValidationState(validationContext)"/>
              </validation-provider>

              <validation-provider :rules="{required: false}" v-slot="validationContext"
                                   v-else-if="['passFromWhomIssue','aboutWork','aboutNoWork'].includes(key)">
                <b-textarea v-model="items[key]" :value="items[key]" :state="getValidationState(validationContext)"/>
              </validation-provider>

              <validation-provider :rules="{required: false}" v-slot="validationContext" v-else>
                <b-form-input v-model="items[key]" :value="items[key]" type="text"
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
  import navBar from "./navBars/navBar";
  import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";

  export default {
    name: "Client",
    components: {
      navBar,
      ValidationProvider,
      ValidationObserver,
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
        data: {model: 'Client'},
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
        $.ajax({
          url: this.$store.state.baseUrl + "api/client/",
          type: "POST",
          data: this.items,
          context: this,
          success: (response) => {
            this.$router.push({name: 'clientView', params: {id: response.data.id}})
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
          }
        });
      },
      notSave() {
        this.$router.push({name: 'mainwindow'})
      },
      getValidationState({dirty, validated, valid = null}) {
        return dirty || validated ? valid : null;
      },
      // getAge(dod) {
      //   var date = new Date(dod);
      //   var ageDifMs = Date.now() - date.getTime();
      //   var ageDate = new Date(ageDifMs);
      //   this.items['age'] = Math.abs(ageDate.getUTCFullYear() - 1970);
      // }
    },
    computed: {
      getAge() {
        var date = new Date(this.items['dod']);
        var ageDifMs = Date.now() - date.getTime();
        var ageDate = new Date(ageDifMs);
        return Math.abs(ageDate.getUTCFullYear() - 1970);
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
    font-size: 35px;
    font-weight: 700;
    padding: 35px 0;
    color: #492727;
    background-color: #D2B48C;
    border-color: #D2B48C
  }

  .card {
    background-color: #f5eed5;
    /*margin-bottom: 5%;*/
  }

  .btn-default {
    background-color: #D2B48C;
    color: #492727;
    margin: 10px;
  }

  .btn-default:hover {
    background-color: #452424;
    color: #D2B48C;
  }

  .my-form {
    background-color: #f5eed5;
  }

  .my-form-group {
    color: #492727;
    margin-right: 3%;
    /*padding-top: 15px;*/
  }
</style>
