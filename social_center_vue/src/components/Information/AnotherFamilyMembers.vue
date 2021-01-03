<template>
  <div class="general">
    <template-info v-bind:url="'anotherFamilyMembers'" v-bind:header="'3. Сведения о членах семьи'"
                   v-bind:subtitle="'3.3 Сведения о других членах семьи'"
                   v-bind:identifier="id" v-bind:identifier_field="'family_member'" ref="template" @addInfo="addInfo"
                   @postInfo="postInfo" class="template-info"></template-info>
    <div class="container" v-if="add">
      <validation-observer ref="observer" v-slot="{ handleSubmit }">
        <b-form @submit.stop.prevent="handleSubmit(save)" @reset="notSave" class="my-form">
          <div v-for="(value,key) in labels" :key="key">
            <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right" class="my-form-group">

              <validation-provider :rules="{required: false}" v-slot="validationContext">
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
    <div v-if="templateBool">
      <MainFooter v-if="this.$refs.template.labels || labels" class="noprint"></MainFooter>
      <!--      <MainFooter v-if="this.$refs.template.labels || choices" class="noprint"></MainFooter>-->
    </div>
  </div>
</template>

<script>
import templateInfo from "../templateInfo";
import {ValidationObserver, ValidationProvider} from "vee-validate/dist/vee-validate.full";
import MainFooter from "../footers/MainFooter";

export default {
  name: "AnotherFamilyMembers",
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
      // choices: '',
      items: '',
      id: '',
      templateBool: false
    }
  },
  created() {
    if (this.$route.params.id !== undefined)
      sessionStorage.setItem('id_another_members', this.$route.params.id);
    this.id = sessionStorage.getItem('id_another_members');
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
        data: {model: 'AnotherFamilyMembers'},
        success: (response) => {
          this.labels = response.data.labels;
          // this.choices = response.data.choices;
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
  }
}
</script>

<style scoped>
@import "../../assets/css/edit-style.css";
</style>
