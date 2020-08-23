<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <div class="card">
        <div class="card-header">Добавление клиента</div>
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
  </div>
</template>

<script>
  import navBar from "./navBar";

  export default {
    name: "Client",
    components: {
      navBar
    },
    data() {
      return {
        items: '',
        labels: '',
        choices: '',
      }
    },
    created() {
      $.ajax({
        url: this.$store.state.baseUrl + "api/fields/",
        type: "GET",
        data: {model: 'Client'},
        success: (response) => {
          this.labels = response.data.labels;
          this.choices = response.data.choices;
          this.items = response.data.items;
        },
        error: (response) => {
          alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      })
    },
    methods: {
      save() {
        $.ajax({
          url: this.$store.state.baseUrl + "api/client/",
          type: "POST",
          data: this.items,
          context: this,
          success: (response) => {
            alert("Данные добавлены.");
            this.$router.push({name: 'mainwindow'})
          },
          error: (response) => {
            alert("Не удалось загрузить данные на сервер.\nПовторите попытку позже.")
          }
        });
      },
      notSave() {
        this.$router.push({name: 'mainwindow'})
      },
      getValidationState({dirty, validated, valid = null}) {
        return dirty || validated ? valid : null;
      },
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 2%;
    text-align: center;
  }

  .card-header {
    display: block;
    font-size: 35px;
    font-weight: 700;
    padding: 35px 0;
    color: #492727;
    background-color: #D2B48C;
    border-color: #D2B48C
  }

  .card {
    background-color: #f5eed5;
    /*margin-bottom: 5%;*/
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
