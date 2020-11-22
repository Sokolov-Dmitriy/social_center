<template>
  <div class="general">
    <template-info v-bind:url="'socialBehavior'" v-bind:header="'1. Сведения о клиенте'"
                   v-bind:subtitle="'1.2 Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя'"
                   v-bind:identifier="id" v-bind:identifier_field="'client'" ref="template"
                   @addInfo="addInfo" @postInfo="postInfo" class="template-info"></template-info>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <b-form-group v-if="labels!=={}" label-cols-sm="3" label-align-sm="right"
                        v-for="(value,key) in labels" :key="key" :label="value" class="my-form-group">
            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-if="'caseExaminedInKDN_ZP'===key">
              <b-form-select :value="items[key]" :options="choices[key]" v-model="items[key]"
                             :state="getValidationState(validationContext)" @change="getKDN_ZP(items[key])">
                <template v-slot:first>
                  <b-form-select-option :value="null"></b-form-select-option>
                </template>
              </b-form-select>
            </validation-provider>

            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="choices[key]">
              <b-form-select :value="items[key]" :options="choices[key]" v-model="items[key]"
                             :state="getValidationState(validationContext)">
                <template v-slot:first>
                  <b-form-select-option :value="null"></b-form-select-option>
                </template>
              </b-form-select>
            </validation-provider>
            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="['durationOfUse','durationOfRemissionD','durationOfRemissionA'].includes(key)">
              <b-form-input type="number" v-model="items[key]" :value="items[key]" step="0.5" min="0" max="99.0"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>
            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="['kindOfDrug','wherePsyRehWasD','wherePsyRehWasA'].includes(key)">
              <b-textarea v-model="items[key]" :value="items[key]"
                          :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-else-if="['dateOfResolutionIPR','DateOfTerminationIPR'].includes(key)">
              <b-form-input type="date" v-model="items[key]" :value="items[key]"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

            <validation-provider :rules="{required: false}" v-slot="validationContext" v-else>
              <b-form-input type="text" v-model="items[key]" :value="items[key]"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>

          </b-form-group>
          <button v-if="!$refs.template.no_data" class="btn btn-default" type="reset">Отмена</button>
          <button class="btn btn-default" type="submit">Добавить</button>
        </b-form>
      </validation-observer>
    </div>
    <div v-if="templateBool">
      <MainFooter v-if="this.$refs.template.labels || choices"></MainFooter>
    </div>
  </div>
</template>

<script>
import templateInfo from "../templateInfo";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import MainFooter from "../footers/MainFooter";

export default {
  name: "ASocialBehavior",
  components: {
    templateInfo,
    ValidationProvider,
    ValidationObserver,
    MainFooter,
  },
  data() {
    return {
      add: false,
      labels: {},
      save_labels: '',
      choices: '',
      id: '',
      templateBool: false
    }
  },
  created() {
    this.id = sessionStorage.getItem('id');
  },
  mounted: function () {
    this.templateBool = true
  },
  methods: {
    addInfo() {

      $.ajax({
        url: this.$store.state.baseUrl + "api/fields/",
        type: "GET",
        data: {model: 'ASocialBehavior'},
        success: (response) => {
          this.save_labels = response.data.labels; //все поля
          this.choices = response.data.choices;
          if (this.$refs.template.edit !== '')
            this.items = this.$refs.template.edit;
          else
            this.items = response.data.items;
          this.startLabels();
          this.add = true;
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      })
    },
    save() {
      this.items['client'] = parseInt(sessionStorage.getItem('id'));
      if (this.$refs.template.edit !== '')
        this.$refs.template.putRequest(this.items);
      else this.$refs.template.postRequest(this.items);
    },
    postInfo() {
      this.add = false;
    },
    notSave() {
      this.$refs.template.labels = this.save_labels;
      this.add = false;
      this.$refs.template.isHide = false;
    },
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
    startLabels() {
      if (this.items['caseExaminedInKDN_ZP'] !== 1) {
        for (var item in this.save_labels)
          if (!['dateOfResolutionIPR', 'resolutionNumber', 'DateOfTerminationIPR', 'terminationNumber'].includes(item))
            this.labels[item] = this.save_labels[item];
      } else this.labels = JSON.parse(JSON.stringify(this.save_labels));
    },
    deleteFields() {
      var array = ['dateOfResolutionIPR', 'resolutionNumber', 'DateOfTerminationIPR', 'terminationNumber'];
      for (var item in array) {
        delete this.labels[array[item]];
        this.items[array[item]] = null;
      }
    },
    getKDN_ZP(value) {
      if (value === 1) this.labels = JSON.parse(JSON.stringify(this.save_labels));
      else this.deleteFields();
    }
  }
}
</script>

<style scoped>
.general {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.template-info {
  flex: 1;
}

.container {
  text-align: center;
  flex: 1000;
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
}
</style>
