<template>
  <div>
    <nav-bar></nav-bar>
    <div class="container">
      <span class="heading">Пользователи</span>
      <input type="text" class="form-search" placeholder="Поиск" v-model="search_text" v-on:input="searchText">
      <button type="button" class="btn btn-add" data-toggle="modal" data-target="#id_user">Добавить пользователя <span
        class="fa fa-plus-circle"></span>
      </button>
      <b-list-group class="list-group">
        <b-list-group-item class="list-group-item" v-for="user in the_users" :key="user.username">
          <div class="edging">
            <h5>Логин: {{user.get('username')}}</h5>
          </div>
          <div class="edging">
            <h5>Имя: {{user.get('first_name')}}</h5>
          </div>
          <div class="edging">
            <h5>Отчество: {{user.get('patronymic')}}</h5>
          </div>
          <div class="edging">
            <h5>Фамилия: {{user.get('last_name')}}</h5>
          </div>
          <div class="edging">
            <h5>Должность: {{user.get('position')}}</h5>
          </div>
          <div class="edging">
            <h5>Почта: {{user.get('email')}}</h5>
          </div>
          <div class="edging" v-if="user.get('username')===admin">
            <h5>Администратор</h5>
          </div>
          <button type="button" class="btn btn-delete" v-if="user.get('username')!==admin"
                  @click="deleteUser(user.get('username'))">Удалить
            <span class="fa fa-trash"></span></button>
        </b-list-group-item>
      </b-list-group>
    </div>
    <div class="modal fade" role="dialog" id="id_user">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header my-header">Новый пользователь</div>
          <form @submit.stop.prevent="newUser" @reset="hideModal">
            <div class="modal-body my-body">
              <div class="form-group">
                <div class="name">Логин</div>
                <input class="input-group" name="login" v-model="new_user.username" required
                       placeholder="Это обязательное поле">
                <div class="name">Пароль</div>
                <input class="input-group" type="password" v-model="new_user.password" required
                       placeholder="Это обязательное поле"
                       v-if="see===false">
                <input class="input-group" type="text" v-model="new_user.password" required
                       placeholder="Это обязательное поле"
                       v-else>
                <a class="fa fa-eye" @click="check" v-if="see===false"></a>
                <a class="fa fa-eye-slash" @click="check" v-else></a>
                <div class="name">Имя</div>
                <input class="input-group" v-model="new_user.first_name">
                <div class="name">Отчество</div>
                <input class="input-group" v-model="new_user.patronymic">
                <div class="name">Фамилия</div>
                <input class="input-group" v-model="new_user.last_name">
                <div class="name">Должность</div>
                <input class="input-group" v-model="new_user.position">
                <div class="name">Почта</div>
                <input class="input-group" type="email" name="email" v-model="new_user.email">
              </div>
            </div>
            <div class="modal-footer my-header">
              <button class="btn btn-done" type="reset">Отмена</button>
              <button type="submit" class="btn btn-done">Ок</button>
            </div>
          </form>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import navBar from "./navBar";

  export default {
    name: "Users",
    components: {
      navBar
    },
    data() {
      return {
        the_users: [],
        search_text: '',
        users: '',
        see: false,
        new_user: {
          username: '',
          password: '',
          first_name: '',
          patronymic: '',
          last_name: '',
          position: '',
          email: ''
        },
        admin: localStorage.getItem('username')
      }
    },
    created() {
      this.getUsers();
    },
    methods: {
      searchText() {
        this.the_users = [];
        for (let i = 0; i < this.users.length; i++) {
          let string = this.users[i].attributes.username + ' ' + this.users[i].attributes.first_name +
            ' ' + this.users[i].attributes.patronymic + ' ' + this.users[i].attributes.last_name + ' ' +
            this.users[i].attributes.position;
          if (string.lastIndexOf(this.search_text) !== -1 || string.toLowerCase().lastIndexOf(this.search_text) !== -1) {
            this.the_users.push(new Map());
            this.the_users[this.the_users.length - 1].set('username', this.users[i].attributes.username);
            this.the_users[this.the_users.length - 1].set('first_name', this.users[i].attributes.first_name);
            this.the_users[this.the_users.length - 1].set('patronymic', this.users[i].attributes.patronymic);
            this.the_users[this.the_users.length - 1].set('last_name', this.users[i].attributes.last_name);
            this.the_users[this.the_users.length - 1].set('position', this.users[i].attributes.position);
            this.the_users[this.the_users.length - 1].set('email', this.users[i].attributes.email);
          }
        }
      },
      getUsers() {
        $.ajax({
          url: this.$store.state.baseUrl+"api/userCrud/",
          type: "GET",
          data: {},
          success: (response) => {
            this.users = response.data;
            this.the_users = [];
            for (let i = 0; i < response.data.length; i++) {
              this.the_users.push(new Map());
              this.the_users[this.the_users.length - 1].set('username', response.data[i].attributes.username);
              this.the_users[this.the_users.length - 1].set('first_name', response.data[i].attributes.first_name);
              this.the_users[this.the_users.length - 1].set('patronymic', response.data[i].attributes.patronymic);
              this.the_users[this.the_users.length - 1].set('last_name', response.data[i].attributes.last_name);
              this.the_users[this.the_users.length - 1].set('position', response.data[i].attributes.position);
              this.the_users[this.the_users.length - 1].set('email', response.data[i].attributes.email);
            }
          },
          error: (response) => {
            if (response.status === 403) {
              this.$router.push({name: 'mainwindow'});
              alert("Недостаточно прав для просмотра страницы.");
            } else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        })
      },
      hideModal() {
        for (var item in this.new_user)
          this.new_user[item] = '';
        $('#id_user').modal('hide');
      },
      newUser() {
        for (var user in this.users)
          if (this.users[user].attributes.username === this.new_user.username) {
            alert("Такой логин уже существует.");
            return;
          }
        for (var item in this.new_user)
          if (this.new_user[item].match(/^[ ]+$/)) {
            this.new_user[item] = '';
            alert("Поле не может состоять из одних пробелов.");
            return;
          }
        $.ajax({
          url: this.$store.state.baseUrl+"api/userCrud/",
          type: "POST",
          data: this.new_user,
          success: (response) => {
            this.getUsers();
            this.hideModal()
          },
          error: (response) => {
            alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
            this.hideModal()
          }
        })
      },
      check() {
        this.see = this.see === false
      },
      deleteUser(username) {
        $.ajax({
          url: this.$store.state.baseUrl+"api/userCrud/",
          type: "DELETE",
          data: {username: username},
          success: (response) => {
            this.getUsers();
          },
          error: (response) => {
            alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
          }
        })
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
    width: 40%;
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

  .form-group {
    padding: 0 40px;
    margin: 0 0 25px 0;
    position: relative;
  }

  .fa-eye {
    display: inline-block;
    position: absolute;
    top: 85px;
    right: 60px;
    font-size: 20px;
    color: #808080;
    transition: all 0.5s ease 0s;
  }

  .fa-eye:hover {
    color: #000;
  }

  .fa-eye-slash {
    display: inline-block;
    position: absolute;
    top: 85px;
    right: 60px;
    font-size: 20px;
    color: #808080;
    transition: all 0.5s ease 0s;
  }

  .fa-eye-slash:hover {
    color: #000;
  }

  .heading {
    display: block;
    font-size: 35px;
    font-weight: 700;
    padding: 20px 0;
    border-bottom: 1px solid #ffffff;
    margin-bottom: 10px;
    color: #492727;
  }

  .container {
    margin-top: 1%;
    text-align: center;
  }

  .list-group {
    position: relative;
    left: 50%;
    transform: translate(-50%, 0);
    /*width: 70%;*/
  }

  .list-group-item {
    margin-top: 10px;
    border-radius: 40px;
    /*f5eed5*/
    background-color: #D2B48C;
    border-color: #D2B48C;
    text-align: left;
  }

  .btn-add {
    background-color: #D2B48C;
    color: #492727;
    margin-bottom: 10px;
    border-radius: 20px;
  }

  .btn-delete {
    background-color: #FFF8DC;
    color: #492727;
    position: relative;
    left: 50%;
    transform: translate(-50%, 0);
    border-radius: 20px;
  }

  .btn-add:hover {
    background-color: #452424;
    color: #D2B48C;
  }

  .btn-delete:hover {
    background-color: #E3DCC3;
    color: #492727;
  }


  .btn-done:hover {
    background-color: #E3DCC3;
    color: #492727;
  }

  .btn-done {
    background-color: #FFF8DC;
    color: #492727;
  }

  h5 {
    color: #492727;
    margin-left: 20px;
    background-color: #FFF8DC;
    border-radius: 20px;
    padding: 5px 5px 5px 30px;
    font-size: 18px;
  }

  /*h5:hover {*/
  /*  background-color: #E3DCC3;*/
  /*  color: #492727;*/
  /*}*/

  .edging {
    margin-top: 10px;
    width: 80%;
    position: relative;
    left: 50%;
    transform: translate(-50%, 0);
  }

  .name {
    color: #492727;
  }

  /deep/ .my-header {
    background-color: #D2B48C;
    color: #492727;
    font-size: 16px;
    font-weight: bolder;
  }

  /deep/ .my-body {
    background-color: #FFF8DC;
  }

  .input-group {
    background-color: #FFF8DC;
    border-color: #FFF8DC;
    outline-color: #FFF8DC;
  }

  @media only screen and (max-width: 990px) {
    .edging {
      width: 100%;
    }
  }

  @media only screen and (max-width: 520px) {
    .form-search {
      width: 100%;
    }

    .btn-add {
      width: 100%;
    }
  }
</style>
