<template>
  <nav class="navbar navbar-expand-lg navbar-light " style="background-color: #D2B48C;padding: 30px;">
    <span class="navbar-brand"><font style="color: #FFF8DC;">КСЦОН</font> Красносельского района</span>
    <span class="navbar-brand" style="color: #0b2e13"></span>
  </nav>
</template>

<script>
export default {
  name: "UnAuthBar"
}
</script>

<style scoped>
.navbar-brand {
  color: #492727 !important;
  font-weight: bolder;
  font-size: 30px;
  position: absolute;
  left: 50%;
  transform: translatex(-50%);
}
@media only screen and (max-width: 379px) {
  .navbar-brand {
    font-size: 16px;
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
}
</style>
