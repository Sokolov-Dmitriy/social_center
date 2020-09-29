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
            <span class="heading">Сброс пароля</span>
            <h5 class="text" v-if="!help_text">Введите свой Email адрес для сброса пароля.</h5>
            <form class="form-group" @submit.stop.prevent="sendEmail" v-if="!help_text">
              <input class="form-control" type="email" placeholder="Email" v-model="email" required>
              <button class="btn btn-default" type="submit">Подтвердить</button>
            </form>
            <h5 class="text" v-if="help_text" v-html="text"/>
            <button class="btn btn-default-center" v-if="help_text" @click="back">Вернуться</button>
            <button class="btn btn-default-right" v-else @click="back">Вернуться</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "EnterEmail",
    data() {
      return {
        email: '',
        help_text: false,
        text: '<p>На указанный Email было отправлено письмо с дальнейшими указаниями для сброса пароля.</p>' +
          '<p>Если Вы не получили письмо, убедитесь, что вы указали правильный Email.</p>'
      }
    },
    methods: {
      sendEmail() {
        $.ajax({
          url: this.$store.state.baseUrl + 'auth/users/reset_password/',
          type: 'POST',
          data: {
            email: this.email
          },
          success: (response) => {
            this.help_text = true;
          },
          error: (response) => {
          }
        })
      },
      back() {
        this.$router.push({name: 'login'})
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

  .btn {
    background-color: #D2B48C;
    color: #492727;
    border-radius: 20px;
    height: 40px;
  }

  .btn:hover {
    background-color: #492727;
    color: #D2B48C;
  }

  .btn-default-right {
    float: left;
    margin-top: 15px;
  }

  .btn-default {
    float: right;
    margin-top: 30px;
  }

  .btn-default-center {
    margin-top: 15px;
  }

  .navbar-brand {
    color: #492727;
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
