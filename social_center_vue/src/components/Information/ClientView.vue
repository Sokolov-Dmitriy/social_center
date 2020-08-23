<template>
  <div>
    <template-info v-bind:url="'client'" v-bind:identifier="id" ref="template" @addInfo="addInfo"
                   v-bind:identifier_field="'client'" @postInfo="postInfo"></template-info>
    <div class="container" v-if="add">
      <b-form @submit.stop.prevent="save" @reset="notSave" class="my-form">
        <b-form-group label-cols-sm="3" :label="labels[key]" label-align-sm="right"
                      v-for="(value,key) in labels" :key="key" class="my-form-group">

          <b-form-input v-if="value === '№' || value==='Количество вз' || value==='Количество детей' "
                        v-model="items[key]" :value="items[key]" type="number" min="0"/>
          <b-form-input v-else-if="value === 'Дата постановки' "
                        v-model="items[key]" :value="items[key]" type="date"/>
          <b-textarea v-else-if="value==='Адрес, телефон' || value==='Дети (ФИО)' " v-model="items[key]"
                      :value="items[key]"/>
          <b-form-input v-else v-model="items[key]" :value="items[key]" type="text"/>
        </b-form-group>
        <button class="btn btn-default" type="reset">Отмена</button>
        <button class="btn btn-default" type="submit">Добавить</button>
      </b-form>
    </div>
  </div>
</template>

<script>
  import templateInfo from "../templateInfo";

  export default {
    name: "ClientView",
    components: {
      templateInfo
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
          url: this.$store.state.baseUrl+"api/fields/",
          type: "GET",
          data: {model: 'Client'},
          success: (response) => {
            this.labels = response.data.labels;
            this.choices = response.data.choices;
            this.items = this.$refs.template.items;
          },
          error: (response) => {
            alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
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
