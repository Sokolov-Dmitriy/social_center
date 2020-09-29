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
            <span class="heading">Новый пароль</span>
            <h5 class="text" v-if="!help_text">Введите новый пароль.</h5>
            <form class="form-group" @submit.stop.prevent="newPassword" v-if="!help_text">
              <input type="password" class="form-control" placeholder="Пароль" v-model="new_password"
                     v-if="see===false">
              <input type="text" class="form-control" placeholder="Пароль" v-model="new_password" v-else>
              <i class="fa fa-lock"></i>
              <a class="fa fa-eye" @click="check" v-if="see===false"></a>
              <a class="fa fa-eye-slash" @click="check" v-else></a>
              <button class="btn btn-default" type="submit">Подтвердить</button>
            </form>
            <h5 class="text" v-if="help_text">Пароль установлен.</h5>
            <h5 class="text" v-if="help_text">Для входа в аккаунт перейдите по ссылке: <a href="#/login">Вход</a></h5>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ConfirmPassword",
    data() {
      return {
        new_password: '',
        see: false,
        help_text: false,
      }
    },
    methods: {
      check() {
        this.see = this.see === false
      },
      newPassword() {
        $.ajax({
          url: this.$store.state.baseUrl + 'auth/users/reset_password_confirm/',
          type: 'POST',
          data: {
            new_password: this.new_password,
            uid: this.$route.params.uid,
            token: this.$route.params.token,
          },
          success: (response) => {
            this.help_text = true;
          },
          error: (response) => {
            if (response.status === 400) {
              var err = JSON.parse(response.responseText);
              alert(err.errors[0].detail);
            }
          }
        })
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

  .text {
    text-align: center;
    color: #492727;
  }

  .form-horizontal .form-control {
    margin-top: 30px;
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

  .form-horizontal .form-group {
    padding: 0 40px;
    margin: 0 0 25px 0;
    position: relative;
  }

  .btn-default {
    background-color: #D2B48C;
    color: #492727;
    border-radius: 20px;
    height: 40px;
    margin-top: 30px;
  }

  .btn-default:hover {
    background-color: #492727;
    color: #D2B48C;
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

  .navbar-brand {
    color: #492727 !important;
    font-weight: bolder;
    font-size: 30px;
    position: absolute;
    left: 50%;
    transform: translatex(-50%);
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
  }

  @media only screen and (max-width: 379px) {
    .navbar-brand {
      font-size: 16px;
    }
  }
</style>
