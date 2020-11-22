<template>
  <footer>
    <div class="logo">
      <img src="static/logo.png" alt="Логотип">
      <p>2020, КЦСОН Красносельского района</p>
    </div>
    <div class="description">
      <p>
        АИС "КЦСОН Красносельского района" -<br>
        автоматизированная информационная<br>
        система, предоставляющая<br>
        функциональные возможности<br>
        хранения, обработки и анализа<br>
        клиентов социального центра<br>
      </p>
    </div>
  </footer>
</template>

<script>
export default {
  name: "MainFooter"
}
</script>

<style scoped>
footer {
  flex: 0 0 auto;
  margin-top: 40px;
  padding: 20px;
  color: white;
  background-color: #d2b68f;
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-around;
}

.logo > p {
  text-align: center;
  margin-top: 10px;
}

.description > p {
  margin-top: 10px;
  text-align: center;
}

img {
  width: 100px;
  height: 100px;
  margin-left: auto;
  margin-right: auto;
  display: block;
  margin-top: 20px;
}

@media (max-width: 700px) {
  .description > p {
    display: none;
  }

  .logo {
    width: 100%;
  }

  img {
    width: 50px;
    height: 50px;
  }
}
</style>
