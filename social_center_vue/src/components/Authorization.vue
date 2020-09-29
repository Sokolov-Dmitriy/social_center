<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light " style="background-color: #D2B48C;padding: 30px;">
      <span class="navbar-brand"><font style="color: #FFF8DC;">КСЦОН</font> Красносельского района</span>
      <span class="navbar-brand" style="color: #0b2e13"></span>
    </nav>
    <div class="container">
      <div class="row align-items-center">
        <div class="offset-md-3 col-md-6">
          <div class="form-horizontal">
            <span class="heading">АВТОРИЗАЦИЯ</span>
            <div class="form-group">
              <input type="text" name="login" class="form-control" placeholder="Логин" v-model="login">
              <i class="fa fa-user"></i>
            </div>
            <div class="form-group help">
              <input type="password" class="form-control" placeholder="Пароль" v-model="password" v-if="see===false">
              <input type="text" class="form-control" placeholder="Пароль" v-model="password" v-else>
              <i class="fa fa-lock"></i>
              <a class="fa fa-eye" @click="check" v-if="see===false"></a>
              <a class="fa fa-eye-slash" @click="check" v-else></a>
            </div>
            <div class="form-group">
              <a class="link" href="#/enterEmail">Я не помню пароль</a>
              <button type="submit" class="btn btn-default" @click="setLogin">ВХОД</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid myfooter">
      <div class="d-flex justify-content-center">
        <h6>2020, КСЦОН Красносельского района</h6>
      </div>
    </div>
  </div>
</template>

<script>
  // import navBar from "./navBar";

  export default {
    name: 'Authorization',
    data() {
      return {
        login: '',
        password: '',
        see: false
      }
    },
    methods: {
      setLogin() {
        $.ajax({
          url: this.$store.state.baseUrl + 'auth/token/login/',
          type: 'POST',
          data: {
            username: this.login,
            password: this.password
          },
          success: (response) => {
            localStorage.setItem('auth_token', response.data.attributes.auth_token);

            localStorage.setItem('username', this.login);
            // this.getUsername();
            this.$router.push({name: 'mainwindow'});
          },
          error: (response) => {
            if (response.status === 400) {
              alert('Введен неправильный логин или пароль.')
            } else alert('Не удалось установить соединение с сервером.\nПовторите попытку позже.')
          }
        })
      },
      check() {
        this.see = this.see === false
      }
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
    /*text-align: center;*/
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

  .form-horizontal .text {
    float: left;
    margin-left: 7px;
    line-height: 20px;
    padding-top: 5px;
    text-transform: capitalize;
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

  .navbar-brand {
    color: #492727;
    font-weight: bolder;
    font-size: 30px;
    position: absolute;
    left: 50%;
    transform: translatex(-50%);
  }

  .link {
    margin-right: 60px;
    color: #492727;
  }

  .btn-default:hover {
    background-color: #492727;
    color: #D2B48C;
  }

  .myfooter {
    position: absolute;
    bottom: 0;
    /*background-color: red;*/
    margin-bottom: 10px;
  }

  @media only screen and (max-width: 992px) {
    .btn {
      margin-top: 20px;
    }
  }

  @media only screen and (max-width: 768px) {
    .btn {
      margin-top: 0;
    }
  }

  @media only screen and (max-width: 580px) {
    .navbar-brand {
      font-size: 25px;
    }
  }

  @media only screen and (max-width: 479px) {
    .navbar-brand {
      font-size: 20px;
    }

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

  @media only screen and (max-width: 388px) {
    .btn {
      margin-top: 20px;
    }
  }

  @media only screen and (max-width: 379px) {
    .navbar-brand {
      font-size: 16px;
    }
  }

</style>
