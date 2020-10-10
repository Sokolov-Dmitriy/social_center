<template>
  <div>
    <div class="container">
      <input type="text" class="form-search" placeholder="Поиск"
             v-model="search_text"
             v-on:input="searchText">
      <button type="button" class="btn my-color"
              @click="$router.push({name: 'client'})">Добавить клиента <span
        class="fa fa-plus-circle"></span></button>
      <div class="card">
        <div class="card-header">Список клиентов</div>
        <div class="scroll">
          <table class="table table-hover">
            <thead class="thead">
            <tr>
              <th scope="col" class="number">№</th>
              <th scope="col" class="code">Код</th>
              <th scope="col">ФИО клиента</th>
            </tr>
            </thead>
            <tbody v-for="client in clients" class="my-tbody">
            <tr @click="$router.push({name: 'clientView', params: {id: client.id}})">
              <td>{{ client.number }}</td>
              <td>{{ client.code }}</td>
              <td>{{ client.full_name }}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {getClientList, searchText} from "../../scripts/mainPage/mainPage";

export default {
  name: "ClientsList",
  data: () => ({
    clients: [],
    search_text: ''
  }),
  created() {
    getClientList()
      .then(
        response => this.clients = response,
        error => {if(error.code===401) this.logOut()}
      );
  },
  methods: {
    searchText() {
      this.clients = searchText(this.search_text);
    }
  }

}
</script>

<style scoped>

.form-search {
  background: #E8E1C6;
  border: none;
  border-radius: 20px;
  box-shadow: none;
  padding: 0 20px 0 45px;
  height: 40px;
  width: 50%;
  transition: all 0.3s ease 0s;
  margin-right: 2%;
  margin-top: 2%;
  margin-bottom: 2%;
}

.form-search:focus {
  background: #DDD6BB;
  box-shadow: none;
  outline: 0 none;
}

.my-color {
  background-color: #D2B48C;
  color: #492727;
  border-radius: 20px;
  margin-right: 2%;
  margin-top: 2%;
  margin-bottom: 2%;
}

.btn:hover {
  background-color: #452424;
  color: #D2B48C;
}

.my-tbody {
  border-color: #f5eed5;
  color: #492727;
}

table {
  table-layout: fixed;
  width: 100%;
}

.scroll {
  height: 400px;
  overflow: auto;
  width: 100%;
}

.card-header {
  display: block;
  font-size: 30px;
  font-weight: 700;
  padding: 25px 0;
  color: #492727;
  background-color: #D2B48C;
  border-color: #D2B48C
}

.card {
  background-color: #f5eed5;
}

.container {
  text-align: center;
  margin-top: 2%;
}

.thead {
  background-color: #D2B48C;
  color: #492727;
}

.code {
  width: 20%;
}

.number {
  width: 20%;
}

@media only screen and (max-width: 520px) {
  .form-search {
    width: 100%;
  }

  .my-color {
    width: 100%;
  }
}

</style>
