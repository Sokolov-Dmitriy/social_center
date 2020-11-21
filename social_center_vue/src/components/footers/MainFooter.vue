<template>
  <footer class="navbar-fixed-bottom">
    <div class="inner">
      <div class="d-flex justify-content-around " style="background-color: #d2b68f; padding-bottom: 10px;">
        <div  >
          <p style="text-align: center; margin-top:10px;"><img src="static/logo.png" alt="lorem"></p>

          <p style="text-align: center;">
            2020, КЦСОН Красносельского района
          </p>
        </div>
        <div class="text">
          <p style="text-align: center;margin-top:10px;">
            АИС "КЦСОН Красносельского района" -<br>
            автоматизированная информационная<br>
            система, предоставляющая<br>
            функциональные возможности<br>
            хранения, обработки и анализа<br>
            клиентов социального центра<br>
          </p>
        </div>

<!--        <div style="">-->
<!--          <form >-->
<!--          <input class="right-el" type="email" placeholder="Почта для связи" style="width: 240px;height: 40px;">-->
<!--          <br>-->
<!--          <textarea class="right-el" placeholder="Сообщение" style="width: 240px;height: 75px;"></textarea>-->
<!--          <br>-->
<!--          <p style="text-align: center;"><input class="right-el input-button" type="submit" value="Отправить"></p>-->
<!--        </form>-->
<!--        </div>-->
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "MainFooter"
}
</script>

<style scoped>
html, body {
  height: 100%;
}
footer{
  display: block;
  position: absolute;
  bottom: 0;
  width: 100%;
  color: white;
}
.right-el{
  margin-top:10px;
  /*border: 2px solid #dadada;*/
  /*border-radius: 2px;*/
}
textarea,input {
  border: 2px solid white; /* some kind of blue border */

  /* other CSS styles */

  /* round the corners */
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;


  /*!* make it glow! *!*/
  /*-webkit-box-shadow: 0px 0px 4px #4195fc;*/
  /*-moz-box-shadow: 0px 0px 4px #4195fc;*/
  /*box-shadow: 0px 0px 4px #4195fc; !* some variation of blue for the shadow *!*/
}
.input-button{
  background-color: #492727;
  border-color: #492727;
  color: white;
  width: 120px;
  height: 28px;
}
img{
  width:100px;
  height:100px;
}
@media (max-width: 700px) {
  .text{
    display: none;
  }
  img{
  width:50px;
  height:50px;
}
}
</style>
