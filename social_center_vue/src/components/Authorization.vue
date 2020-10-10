<template>
  <div>
    <un-auth-bar></un-auth-bar>
    <div class="container">
      <div class="row align-items-center">
        <div class="offset-md-3 col-md-6">
          <div class="form-horizontal">
            <span class="heading">АВТОРИЗАЦИЯ</span>
            <div class="form-group">
              <input type="text" name="login" class="form-control" placeholder="Логин" v-model="authData.username">
              <i class="fa fa-user"></i>
            </div>
            <div class="form-group help">
              <input type="password" class="form-control" placeholder="Пароль" v-model="authData.password"
                     v-if="see===false">
              <input type="text" class="form-control" placeholder="Пароль" v-model="authData.password" v-else>
              <i class="fa fa-lock"></i>
              <a class="fa fa-eye" @click="see=!see" v-if="see===false"></a>
              <a class="fa fa-eye-slash" @click="see=!see" v-else></a>
            </div>
            <div class="form-group d-inline-flex pl-0 pr-0">
              <div class="align-self-center">
                <a class="link mr-sm-6 mr-md-6" href="#/enterEmail">Я не помню пароль</a>
              </div>
              <div>
                <button type="submit" class="btn btn-default" @click="logIn(authData)">ВХОД</button>
              </div>
            </div>
            <div style="color: red" v-if="showError">
              Неверный логин/пароль
            </div>
          </div>
        </div>
      </div>
    </div>
    <common-footer></common-footer>
  </div>
</template>

<script>
import {getToken} from "../scripts/authorization/auth";
import commonFooter from "./footers/commonFooter";
import UnAuthBar from "./navBars/UnAuthBar";

export default {
  name: 'Authorization',
  components: {
    commonFooter,
    UnAuthBar
  },
  data: () => ({
    authData: {
      username: "",
      password: "",
    },
    see: false,
    showError: false,
  }),

  methods: {
    logIn() {
      getToken(this.authData)
        .then(
          response => {
            localStorage.setItem('auth_token', response);
            localStorage.setItem('username', this.authData.username);
            this.$router.push({name: 'mainwindow'});
          },
          error => this.showError = true
        );
    },
  }
}
</script>

<style scoped>

.form-horizontal {
  text-align: center !important;
  background: #FFF8DC;
  padding-bottom: 40px;
  border-radius: 15px;
  margin-top: 10%;
}

.form-horizontal .heading {
  display: block;
  font-size: 35px;
  font-weight: 700;
  padding: 35px 0;
  border-bottom: 1px solid #ffffff;
  margin-bottom: 30px;
  color: #492727;
}

.form-horizontal .form-group {
  padding: 0 40px;
  margin: 0 0 25px 0;
  position: relative;
}

.form-horizontal .form-control {
  background: #ffffff;
  border: none;
  border-radius: 20px;
  box-shadow: none;
  padding: 0 20px 0 45px;
  height: 40px;
  transition: all 0.3s ease 0s;
}

.form-horizontal .form-control:focus {
  background: #ffffff;
  box-shadow: none;
  outline: 0 none;
}

.form-horizontal .form-group i {
  position: absolute;
  top: 12px;
  left: 60px;
  font-size: 17px;
  color: #ffffff;
  transition: all 0.5s ease 0s;
}

.form-horizontal .form-control:focus + i {
  color: #D2B48C;
}

.form-horizontal .fa-eye {
  display: inline-block;
  position: absolute;
  top: 12px;
  right: 60px;
  font-size: 20px;
  color: #808080;
  transition: all 0.5s ease 0s;
}

.form-horizontal .fa-eye:hover {
  color: #000;
}

.form-horizontal .fa-eye-slash {
  display: inline-block;
  position: absolute;
  top: 12px;
  right: 60px;
  font-size: 20px;
  color: #808080;
  transition: all 0.5s ease 0s;
}

.form-horizontal .fa-eye-slash:hover {
  color: #000;
}

.form-horizontal .btn {
  font-size: 14px;
  color: #492727;
  background: #D2B48C;
  border-radius: 30px;
  padding: 10px 25px;
  border: none;
  text-transform: capitalize;
  transition: all 0.5s ease 0s;
}

.link {
  margin-right: 60px;
  color: #492727;
}

.btn-default:hover {
  background-color: #492727;
  color: #D2B48C;
}


@media only screen and (max-width: 479px) {

  .form-horizontal .form-group {
    padding: 0 25px;
  }

  .form-horizontal .form-group i {
    left: 45px;
  }

  .form-horizontal .btn {
    padding: 10px 20px;
  }
}

</style>
