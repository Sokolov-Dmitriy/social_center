<template>
  <div class="general">
    <template-info v-bind:url="'familyMembers'" v-bind:header="'3. Сведения о членах семьи'"
                   v-bind:subtitle="'3.1 Общие сведения'"
                   v-bind:identifier="id" v-bind:identifier_field="'client'" ref="template" @addInfo="addInfo"
                   @postInfo="postInfo" class="template-info"></template-info>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right"
                        v-for="(value,key) in labels" :key="key" class="my-form-group">
            <validation-provider :rules="{required:false}" v-slot="validationContext">
              <b-form-select :value="items[key]" :options="choices[key]" v-model="items[key]"
                             :state="getValidationState(validationContext)">
                <template v-slot:first>
                  <b-form-select-option :value="null"></b-form-select-option>
                </template>
              </b-form-select>
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
  name: "FamilyMembers",
  components: {
    templateInfo,
    ValidationProvider,
    ValidationObserver,
    MainFooter,
  },
  data() {
    return {
      add: false,
      labels: '',
      choices: '',
      items: '',
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
      this.add = true;
      $.ajax({
        url: this.$store.state.baseUrl + "api/fields/",
        type: "GET",
        data: {model: 'FamilyMembersInformation'},
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
      this.items['client'] = parseInt(sessionStorage.getItem('id'));
      if (this.$refs.template.edit !== '')
        this.$refs.template.putRequest(this.items);
      else this.$refs.template.postRequest(this.items);
    },
    postInfo() {
      this.add = false;
    },
    notSave() {
      this.$refs.template.labels = this.labels;
      this.add = false;
      this.$refs.template.isHide = false;
    },
    getValidationState({dirty, validated, valid = null}) {
      return dirty || validated ? valid : null;
    },
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
