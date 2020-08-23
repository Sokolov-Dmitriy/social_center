<template>
  <div>
    <div class="container">
<!--           <a href="javascript:window.print()">fff</a>-->
      <input type="text" class="form-search" placeholder="Поиск" v-model="search_text" v-on:input="searchText">
      <button type="button" class="btn my-color" @click="addClient">Добавить клиента <span
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
            <tr @click="openInfo(client.get('id'))">
              <td>{{client.get('number')}}</td>
              <td>{{client.get('code')}}</td>
              <td>{{client.get('full_name')}}</td>
            </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {

    name: "ClientsList",


    data() {
      return {
        clinets: '',
        clients: [],
        search_text: ''
      }
    },

    created() {
      $.ajaxSetup({
        headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
      });
      this.loadClients()
    },
    methods: {
      searchText() {

        this.clients = [];
        for (let i = 0; i < this.clinets.length; i++) {
          let string = this.clinets[i].attributes.number + ' ' + this.clinets[i].attributes.code + ' ' + this.clinets[i].attributes.full_name;
          if (string.lastIndexOf(this.search_text) !== -1 || string.toLowerCase().lastIndexOf(this.search_text) !== -1) {
            this.clients.push(new Map());
            this.clients[this.clients.length - 1].set('number', this.clinets[i].attributes.number);
            this.clients[this.clients.length - 1].set('code', this.clinets[i].attributes.code);
            this.clients[this.clients.length - 1].set('full_name', this.clinets[i].attributes.full_name);
            this.clients[this.clients.length - 1].set('id', this.clinets[i].id);

          }
        }
        // console.log(this.clinets);

      },
      loadClients() {
        $.ajax({
          url: this.$store.state.baseUrl+"api/clients/",
          type: "GET",
          success: (response) => {
            // console.log(response.data);
            this.clinets = response.data;
            for (let i = 0; i < response.data.length; i++) {
              this.clients.push(new Map());
              this.clients[this.clients.length - 1].set('number', response.data[i].attributes.number);
              this.clients[this.clients.length - 1].set('code', response.data[i].attributes.code);
              this.clients[this.clients.length - 1].set('full_name', response.data[i].attributes.full_name);
              this.clients[this.clients.length - 1].set('id', response.data[i].id);
            }
            // console.log(this.clients);
          }
        })
      },
      addClient() {
        this.$router.push({name: 'client'})
      },
      openInfo(id) {
        this.$router.push({name: 'clientView', params: {id: id}})
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
  /* @media only screen and (max-width: 750px) {*/
  /* .code {*/
  /*    width: 30%;*/
  /*  }*/
  /*}*/

</style>
