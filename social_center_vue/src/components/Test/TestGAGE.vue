<template>
  <div>
    <template-test v-bind:url="'testGAGE'" v-bind:identifier="id" ref="template" @addInfo="addInfo"
                   v-bind:header="'Тест GAGE'" v-bind:identifier_field="'test'"
                   @postInfo="postInfo" @newID="newID"></template-test>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <div v-if="key!=='attempt'" v-for="(value,key) in labels" :key="key">
            <div v-if="key==='loss_documents' && labels[key]" class="my-block">3. Оценка риска злоупотребления ПАВ* (*–
              как только
              клиент набирает 3
              балла в этом разделе, можно переходить к разделу 4, можно задавать не все вопросы из перечня)
            </div>
            <div v-if="key==='dose_reduction' && labels[key]" class="my-block">4. Вопросы о риске зависимости</div>
            <b-form-group :label="labels[key]" label-align-sm="left" v-if="labels[key]"
                          class="my-form-group">
              <validation-provider rules="required" v-slot="validationContext"
                                   v-if="['alcohol','substances'].includes(key)">
                <b-form-radio-group :options="choices[key]" v-model="items[key]" :value="items[key]"
                                    :state="getValidationState(validationContext)" @input="choiceYes(key,items[key])"
                                    class="my-radio"></b-form-radio-group>
              </validation-provider>
              <validation-provider :rules="{required: false}" v-slot="validationContext" v-else-if="choices[key]">
                <b-form-radio-group v-if="!['loss_documents','do_not_work','lots_alcohol'].includes(key)"
                                    :options="choices[key]" v-model="items[key]" :value="items[key]"
                                    :state="getValidationState(validationContext)"
                                    class="my-radio"></b-form-radio-group>
                <b-form-radio-group v-else :options="choices[key]" v-model="items[key]" :value="items[key]"
                                    :state="getValidationState(validationContext)"
                                    @input="choiceSubsection(key,items[key])"
                                    class="my-radio"></b-form-radio-group>
              </validation-provider>
              <validation-provider :rules="{required: false}" v-slot="validationContext" v-else>
                <b-textarea v-model="items[key]" :value="items[key]" :state="getValidationState(validationContext)"/>
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
  import templateTest from "./templateTest";
  import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";

  export default {
    name: "TestGAGE",
    components: {
      templateTest,
      ValidationProvider,
      ValidationObserver,
    },
    data() {
      return {
        add: false,
        labels: '',
        choices: '',
        items: '',
        id: '',
        attempt: '',
        save_labels: ''
      }
    },
    created() {
      if (this.$route.params.id !== undefined && this.$route.params.attempt) {
        sessionStorage.setItem('id_test', this.$route.params.id);
        sessionStorage.setItem('test_attempt', this.$route.params.attempt);
      }
      this.id = sessionStorage.getItem('id_test');
      this.attempt = sessionStorage.getItem('test_attempt');
    },
    methods: {
      choiceSubsection(key, choice) {
        var fields_loss_documents = ['loss_documents_when', 'loss_documents_time'];
        var fields_do_not_work = 'do_not_work_when';
        var fields_lots_alcohol = 'lots_alcohol_time';
        if (key === 'loss_documents') {
          if (choice === 0) {
            for (var item in fields_loss_documents) {
              this.labels[fields_loss_documents[item]] = null;
              this.items[fields_loss_documents[item]] = null;
            }
          } else if (choice === 1) {
            for (var item in fields_loss_documents)
              this.labels[fields_loss_documents[item]] = this.save_labels[fields_loss_documents[item]];
          }
        }

        if (key === 'do_not_work') {
          if (choice === 0) {
            this.labels[fields_do_not_work] = null;
            this.items[fields_do_not_work] = null;
          } else if (choice === 1) {
            this.labels[fields_do_not_work] = this.save_labels[fields_do_not_work];
          }
        }


        if (key === 'lots_alcohol') {
          if (choice === 0) {
            this.labels[fields_lots_alcohol] = null;
            this.items[fields_lots_alcohol] = null;
          } else if (choice === 1) {
              this.labels[fields_lots_alcohol] = this.save_labels[fields_lots_alcohol];
          }
        }
      },
      choiceYes(key, choice) {
        var fields_all = ['loss_documents', 'loss_documents_when', 'loss_documents_time', 'dose_reduction',
          'irritation', 'fault', 'tone'];
        var fields_alcohol = ['do_not_work', 'do_not_work_when', 'loss_loved_ones', 'fight', 'injuries', 'lots_alcohol',
          'lots_alcohol_time', 'drink_alcohol_time'];
        var fields_substances = ['try_substances', 'try_substances_choice', 'how_use', 'difficulties', 'poor_health',
          'company'];
        if (this.items['alcohol'] === 0 && this.items['substances'] === 0) {
          for (var item in fields_all) {
            this.labels[fields_all[item]] = null;
            this.items[fields_all[item]] = null;
          }
        } else {
          for (var item in fields_all)
            this.labels[fields_all[item]] = this.save_labels[fields_all[item]];
        }
        if (key === 'alcohol') {
          if (choice === 0) {
            for (var item in fields_alcohol) {
              this.labels[fields_alcohol[item]] = null;
              this.items[fields_alcohol[item]] = null;
            }
          } else if (choice === 1) {
            for (var item in fields_alcohol)
              this.labels[fields_alcohol[item]] = this.save_labels[fields_alcohol[item]];
          }
        } else if (key === 'substances') {
          if (choice === 0) {
            for (var item in fields_substances) {
              this.labels[fields_substances[item]] = null;
              this.items[fields_substances[item]] = null;
            }
          } else if (choice === 1) {
            for (var item in fields_substances)
              this.labels[fields_substances[item]] = this.save_labels[fields_substances[item]];
          }
        }
      },
      addInfo() {
        this.add = true;
        $.ajax({
          url: this.$store.state.baseUrl + "api/fields/",
          type: "GET",
          data: {model: 'TestGAGE'},
          success: (response) => {
            this.labels = JSON.parse(JSON.stringify(response.data.labels));
            this.save_labels = response.data.labels;
            this.choices = response.data.choices;
            if (this.$refs.template.edit !== '')
              this.items = this.$refs.template.edit;
            else
              this.items = response.data.items;
            this.choiceYes('alcohol', this.items['alcohol']);
            this.choiceYes('substances', this.items['substances']);

            this.choiceSubsection('loss_documents', this.items['loss_documents']);
            this.choiceSubsection('do_not_work', this.items['do_not_work']);
            this.choiceSubsection('lots_alcohol', this.items['lots_alcohol']);
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        })
      },
      save() {
        this.items['client'] = parseInt(sessionStorage.getItem('id'));
        this.items['attempt'] = parseInt(sessionStorage.getItem('test_attempt'));
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
      newID(id) {
        sessionStorage.setItem('id_test', id);
        this.id = id;
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
    background: #EDE5C9;
    margin-right: 3%;
    margin-left: 3%;
  }

  .my-radio {
    text-align: left;
    font-size: 14px;
    /*margin-left: 5%;*/
    padding: 10px;
  }

  /deep/ .custom-control {
    /*padding-top: 10px;*/
    display: block;
  }

  /deep/ .text-sm-left {
    /*margin-top: 2%;*/
    font-weight: bold;
    background: #EDE5C9;
  }

  .my-block {

    text-align: left;
    color: #492727;
    margin-right: 3%;
    margin-left: 3%;
    font-size: 18px;
    padding: 3%;
  }
</style>
