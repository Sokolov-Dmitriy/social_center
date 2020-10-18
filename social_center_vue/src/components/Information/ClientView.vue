<template>
  <div>
    <template-info v-bind:url="'client'" v-bind:header="'1. Сведения о клиенте'"
                   v-bind:subtitle="'1.1. Общая информация'"
                   v-bind:identifier="id" ref="template"
                   @addInfo="addInfo"
                   v-bind:identifier_field="'client'" @postInfo="postInfo"></template-info>
    <div class="container" v-if="add">
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
                                 v-else-if="['dateOfInterview','dateOfCertified','passDateIssue'].includes(key)">
              <b-form-input v-model="items[key]" :value="items[key]" type="date"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="'dod'===key">
              <b-form-input v-model="items[key]" :value="items[key]" type="date" @change="getAge(items[key])"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="['age','adultsCount','minorsCount'].includes(key)">
              <b-form-input v-model="items[key]" :value="items[key]" type="number" min="0"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false,length:6}" v-slot="validationContext"
                                 v-else-if="['passNumber','addressIndex'].includes(key)">
              <b-form-input v-model="items[key]" :value="items[key]" type="number"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false,length:4}" v-slot="validationContext"
                                 v-else-if="'passSeries'===key">
              <b-form-input v-model="items[key]" :value="items[key]" type="number"
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
</template>

<script>
  import templateInfo from "../templateInfo";
  import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";

  export default {
    name: "ClientView",
    components: {
      templateInfo,
      ValidationProvider,
      ValidationObserver,
    },
    data() {
      return {
        add: false,
        labels: '',
        choices: '',
        items: '',
        id: ''
      }
    },
    created() {
      if (this.$route.params.id !== undefined)
        sessionStorage.setItem('id', this.$route.params.id);
      this.id = sessionStorage.getItem('id');
    },
    methods: {
      addInfo() {
        this.add = true;
        $.ajax({
          url: this.$store.state.baseUrl + "api/fields/",
          type: "GET",
          data: {model: 'Client'},
          success: (response) => {
            this.labels = response.data.labels;
            this.choices = response.data.choices;
            if (this.$refs.template.edit !== '')
              this.items = this.$refs.template.edit;
            else
              this.items = response.data.items;
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        })
      },
      save() {
        this.$refs.template.putRequest(this.items);
      },
      postInfo() {
        this.add = false;
      },
      notSave() {
        this.add = false;
        this.$refs.template.isHide = false;
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
    },
    // computed: {
    //   getAge() {
    //     if (this.items['dod'] !== null) {
    //       var date = new Date(this.items['dod']);
    //       var ageDifMs = Date.now() - date.getTime();
    //       var ageDate = new Date(ageDifMs);
    //       return Math.abs(ageDate.getUTCFullYear() - 1970);
    //     }
    //     return "";
    //   }
    // }
  }
</script>

<style scoped>
  .btn-default {
    background-color: #D2B48C;
    color: #492727;
    margin: 10px;
  }

  .btn-default:hover {
    background-color: #452424;
    color: #D2B48C;
  }

  .container {
    text-align: center;
  }

  .my-form {
    background-color: #f5eed5;
  }

  .my-form-group {
    color: #492727;
    margin-right: 3%;
  }
</style>
