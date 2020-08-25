<template>
  <div>
    <template-test v-bind:url="'testSOCRATES'" v-bind:identifier="id" ref="template" @addInfo="addInfo"
                   v-bind:header="'Тест SOCRATES'" v-bind:identifier_field="'test'"
                   @postInfo="postInfo" @newID="newID"></template-test>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <b-form-group :label="labels[key]" label-align-sm="left"
                        v-if="key!=='attempt'" v-for="(value,key) in labels" :key="key" class="my-form-group">

            <validation-provider rules="required" v-slot="validationContext">
              <b-form-select :options="choices[key]" v-model="items[key]" :value="items[key]"
                             :state="getValidationState(validationContext)"></b-form-select>
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
  import templateTest from "./templateTest";
  import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";

  export default {
    name: "TestSOCRATES",
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
      addInfo() {
        this.add = true;
        $.ajax({
          url: this.$store.state.baseUrl + "api/fields/",
          type: "GET",
          data: {model: 'TestSOCRATES'},
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
    margin-right: 3%;
    margin-left: 3%;
    /*margin-top: 3%;*/
  }

</style>
