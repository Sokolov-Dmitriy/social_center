<template>
  <div class="general">
    <nav-bar ref="nav"></nav-bar>
    <div class="container">
      <span class="heading">Информация о пользователе</span>
      <b-input-group style="margin-top: 2%">
        <template v-slot:prepend>
          <b-input-group-text style="color: #492727;background-color: #D2B48C">Логин</b-input-group-text>
        </template>
        <b-form-input readonly :value="username" style="background-color: white;"></b-form-input>
        <template v-slot:append>
          <button class="btn fa fa-edit" type="button" data-toggle="modal" data-target="#id_other"
                  @click="setOther('Логин')"></button>
        </template>
      </b-input-group>
      <form @submit.stop.prevent="showPasswordForm">
        <b-input-group style="margin-top: 2%">
          <template v-slot:prepend>
            <b-input-group-text style="color: #492727;background-color: #D2B48C">Пароль</b-input-group-text>
          </template>
          <b-form-input placeholder="Текущий пароль:" type="password" required v-model="password"/>
          <template v-slot:append>
            <button class="btn fa fa-edit" type="submit"></button>
          </template>
        </b-input-group>
      </form>

      <b-input-group style="margin-top: 2%"
                     v-for="name in [['Имя',this.items.first_name],['Отчество',this.items.patronymic],['Фамилия',this.items.last_name],['Должность',this.items.position],['Почта',this.items.email]]"
                     :key="name[0]">
        <template v-slot:prepend>
          <b-input-group-text style="color: #492727;background-color: #D2B48C" readonly>{{ name[0] }}
          </b-input-group-text>
        </template>
        <b-form-input readonly :value="name[1]" style="background-color: white;"></b-form-input>
        <template v-slot:append>
          <button class="btn fa fa-edit" type="button" @click="setOther(name[0])"
                  data-toggle="modal" data-target="#id_other"></button>
        </template>
      </b-input-group>
    </div>

    <div class="modal fade" role="dialog" id="id_other">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header my-header">{{ header }}</div>
          <form ref="form" @submit.stop.prevent="newOther" @reset="hideModal('id_other')">
            <div class="modal-body my-body">
              <input class="input-group" v-if="header==='Почта'" type="email" name="email" v-model="new_other">
              <input class="input-group" v-else-if="header==='Логин'" name="login" required v-model="new_other">
              <div class="form-group" v-else-if="header==='Пароль'">
                <input class="input-group" type="password" v-model="new_password" required v-if="see===false">
                <input class="input-group" type="text" v-model="new_password" required v-else>
                <a class="fa fa-eye" @click="check" v-if="see===false"></a>
                <a class="fa fa-eye-slash" @click="check" v-else></a>
              </div>
              <input class="input-group" type="text" v-model="new_other" v-else>
            </div>
            <div class="modal-footer my-header">
              <button class="btn btn-default" type="reset">Отмена</button>
              <button type="submit" class="btn btn-default">Ок</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <MainFooter></MainFooter>
  </div>
</template>

<script>
import navBar from "./navBars/navBar";
import MainFooter from "./footers/MainFooter";

export default {
  name: "Profile",
  components: {
    navBar,
    MainFooter
  },
  data() {
    return {
      items: '',
      username: '',
      password: '',
      new_password: '',
      see: false,
      header: '',
      new_other: ''
    }
  },
  created() {
    this.getData();
  },
  methods: {
    getData() {
      $.ajax({
        url: this.$store.state.baseUrl + "api/user/",
        type: "GET",
        data: {},
        success: (response) => {
          this.items = response.data[0].attributes;
          this.username = this.items.username;
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      })
    },
    hideModal(id) {
      id = '#' + id;
      this.new_password = '';
      this.new_other = '';
      $(id).modal('hide');
    },
    newLogin() {
      if (this.new_other === this.username) alert("Новый логин не должен совпадать с предыдущим.");
      else
        $.ajax({
          url: this.$store.state.baseUrl + "auth/users/set_username/",
          type: "POST",
          data: {
            new_username: this.new_other
          },
          success: (response) => {
            localStorage.setItem('username', this.new_other);
            this.$refs.nav.getUsername();
            this.getData();
            this.hideModal('id_other')
          },
          error: (response) => {
            this.hideModal('id_other');
            if (response.status === 401) this.logOut(); else
              alert("Не удалось установить соединение с сервером.\nПовторите попытку позже");
          }
        })
    },
    newPassword() {
      $.ajax({
        url: this.$store.state.baseUrl + "auth/users/set_password/",
        type: "POST",
        data: {
          current_password: this.password,
          new_password: this.new_password
        },
        success: (response) => {
          this.password = '';
          this.hideModal('id_other')
        },
        error: (response) => {
          if (response.status === 401) {
            this.hideModal('id_other');
            this.logOut();
            return;
          }
          if (response.status === 400) {
            var err = JSON.parse(response.responseText);
            alert(err.errors[0].detail);
          } else {
            alert("Не удалось установить соединение с сервером.\nПовторите попытку позже.");
            this.hideModal('id_other')
          }
        }
      })
    },
    check() {
      this.see = this.see === false
    },
    setOther(header) {
      this.header = header;
    },
    newOther() {
      var data = {};
      switch (this.header) {
        case 'Логин':
          this.newLogin();
          return;
        case 'Пароль':
          this.newPassword();
          return;
        case 'Имя':
          data['first_name'] = this.new_other;
          break;
        case 'Отчество':
          data['patronymic'] = this.new_other;
          break;
        case 'Фамилия':
          data['last_name'] = this.new_other;
          break;
        case 'Должность':
          data['position'] = this.new_other;
          break;
        case 'Почта':
          data['email'] = this.new_other;
          break;
      }
      $.ajax({
        url: this.$store.state.baseUrl + "api/user/",
        type: "PUT",
        data: data,
        success: (response) => {
          this.getData();
          this.hideModal('id_other')
        },
        error: (response) => {
          this.hideModal('id_other');
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      })
    },
    showPasswordForm() {
      this.setOther('Пароль');
      $('#id_other').modal('show');
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

.container {
  flex: 1;
}

.form-group {
  padding: 0 40px;
  margin: 0 0 25px 0;
  position: relative;
}

.fa-eye {
  display: inline-block;
  position: absolute;
  top: 4px;
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
  top: 4px;
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
  padding: 30px 0;
  border-bottom: 1px solid #ffffff;
  margin-bottom: 30px;
  color: #492727;
}

.container {
  margin-top: 1%;
  text-align: center;
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

.btn {
  background-color: #FFF8DC;
  color: #492727;
}

.btn:hover {
  background-color: #E3DCC3;
  color: #492727;
}

.fa-edit {
  background-color: #D2B48C;
  color: #492727;
  font-size: 20px;
}

.fa-edit:hover {
  background-color: #452424;
  color: #D2B48C;
}

@media only screen and (max-width: 1800px) {
  .container {
    width: 50%;
  }
}

@media only screen and (max-width: 1199px) {
  .container {
    width: 60%;
  }
}

@media only screen and (max-width: 991px) {
  .container {
    width: 70%;
  }
}

@media only screen and (max-width: 767px) {
  .container {
    width: 100%;
  }
}
</style>
