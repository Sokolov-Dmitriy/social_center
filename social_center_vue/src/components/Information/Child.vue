<template>
  <div class="general">
    <template-info v-bind:url="'child'" v-bind:identifier="id" ref="template" @addInfo="addInfo"
                   v-bind:identifier_field="'child'"
                   @postInfo="postInfo" class="template-info"></template-info>
    <div class="container" v-if="add">
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
                              :state="getValidationState(validationContext)" type="date" @change="getAge(items[key])"/>
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
    <div v-if="templateBool">
      <MainFooter v-if="this.$refs.template.labels || choices" class="noprint"></MainFooter>
    </div>
  </div>
</template>

<script>
import templateInfo from "../templateInfo";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import MainFooter from "../footers/MainFooter";

export default {
  name: "Child",
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
    if (this.$route.params.id !== undefined)
      sessionStorage.setItem('id_child', this.$route.params.id);
    this.id = sessionStorage.getItem('id_child');
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
        data: {model: 'Child'},
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
      this.$refs.template.labels = this.labels;
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

.my-block {
  text-align: center;
  color: #492727;
  font-size: 18px;
  padding: 3%;
}

@media print {
  .noprint {
    display: none;
  }
}
</style>
