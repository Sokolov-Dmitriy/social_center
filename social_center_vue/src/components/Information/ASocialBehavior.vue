<template>
  <div>
    <template-info v-bind:url="'socialBehavior'" v-bind:header="'1. Сведения о клиенте'"
                   v-bind:subtitle="'1.2 Информация о противоправных действиях, правонарушениях, употреблении наркотиков, алкоголя'"
                   v-bind:identifier="id" v-bind:identifier_field="'client'" ref="template"
                   @addInfo="addInfo" @postInfo="postInfo"></template-info>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right"
                        v-for="(value,key) in labels" :key="key" class="my-form-group">
            <!--            v-if="key!=='client'"-->
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
                                 v-if="['durationOfUse','durationOfRemissionD','durationOfRemissionA'].includes(key)">
              <b-form-input type="number" v-model="items[key]" :value="items[key]" step="0.5" min="0.0" max="99.0"
                            :state="getValidationState(validationContext)"/>
            </validation-provider>
            <validation-provider :rules="{required: false}" v-slot="validationContext"
                                 v-if="['kindOfDrug','wherePsyRehWasD','wherePsyRehWasA'].includes(key)">
              <b-textarea v-model="items[key]" :value="items[key]"
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
    name: "ASocialBehavior",
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
        id: ''
      }
    },
    created() {
      this.id = sessionStorage.getItem('id');
    },
    methods: {
      addInfo() {
        this.add = true;
        $.ajax({
          url: this.$store.state.baseUrl+"api/fields/",
          type: "GET",
          data: {model: 'ASocialBehavior'},
          success: (response) => {
            // console.log(response.data)
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
