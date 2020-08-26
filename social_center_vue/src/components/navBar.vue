<template>


  <nav class="navbar navbar-expand-lg navbar-light color-ser">
    <a class="navbar-brand" href="#/"><span class="fa fa-home fa-2x"></span></a>
    <a class="navbar-brand marg-left" href="#/table"><span class="fa fa-table fa-2x"></span></a>
    <button class="btn" onclick="window.print()"><span class="fa fa-print fa-2x"></span></button>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
      </ul>
      <form class="dropdown my-2 my-lg-0 marg">
        <a class="nav-link dropdown-toggle" id="navbarDropdown" role="button" data-toggle="dropdown"
           aria-haspopup="true" aria-expanded="false">
          {{username}}
        </a>
        <div class="dropdown-menu color-ser" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#/users">Пользователи</a>
          <a class="dropdown-item" href="#/profile">Профиль</a>
          <a class="dropdown-item" @click="signOut">Выход</a>
        </div>
      </form>
    </div>
  </nav>
</template>

<script>
  import "bootstrap/dist/js/bootstrap.bundle.js"

  export default {
    name: "navBar",
    data() {
      return {
        username: ''
      }
    },

    beforeMount() {
      this.getUsername()
    },
    methods: {
      getUsername() {
        this.username = localStorage.getItem('username');
      },


      signOut() {
        $.ajax({
          url: this.$store.state.baseUrl + 'auth/token/logout/',
          type: 'POST',
          success: (response) => {
            // console.log(response.data);
            this.logOut();
          }
        })
      }
    }
  }
</script>

<style scoped>
  .color-ser {
    background-color: #D2B48C;
    z-index: 999999;
  }

  .dropdown-item:hover {
    background-color: #BA9F7D;
    color: black;
  }

  .marg {
    margin-right: 70px;
  }

  .marg-left {
    margin-left: 10px;
  }

  span {
    color: #492727;
  }

  span:hover {
    /*background-color: #C6AA85;*/
    color: #391E1E;
  }

  a {
    color: #492727;
  }
</style>
