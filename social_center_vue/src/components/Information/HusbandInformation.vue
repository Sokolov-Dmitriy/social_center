<template>
  <div>
    <template-info v-bind:url="'husbandInformation'" v-bind:header="'3. Сведения о членах семьи'"
                   v-bind:subtitle="'3.2 Информация о муже/партнёре'"
                   v-bind:identifier="id" v-bind:identifier_field="'husband'" ref="template" @addInfo="addInfo"
                   @postInfo="postInfo"></template-info>
    <div class="container" v-if="add">
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
</template>

<script>
import templateInfo from "../templateInfo";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";

export default {
  name: "HusbandInformation",
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
      sessionStorage.setItem('id_husband', this.$route.params.id);
    this.id = sessionStorage.getItem('id_husband');
  },
  methods: {
    addInfo() {
      this.add = true;
      $.ajax({
        url: this.$store.state.baseUrl + "api/fields/",
        type: "GET",
        data: {model: 'HusbandInformation'},
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
      if(dateNow.getFullYear() > date.getFullYear()){
        this.items['age'] =  Math.abs(ageDate.getUTCFullYear() - 1970);
      }else {
        if(dateNow.getFullYear() < date.getFullYear()){
          this.items['age'] = -1;
        }else {
          if(dateNow.getMonth() > date.getMonth()){
            this.items['age'] =  Math.abs(ageDate.getUTCFullYear() - 1970);
          }else {
            if(dateNow.getMonth() < date.getMonth()){
              this.items['age'] = -1;
            }else {
              if(dateNow.getDate() >= date.getDate()){
                this.items['age'] =  Math.abs(ageDate.getUTCFullYear() - 1970);
              }else {
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

.my-little-block {
  text-align: center;
  color: #492727;
  font-size: 16px;
  padding: 2%;
}
</style>
