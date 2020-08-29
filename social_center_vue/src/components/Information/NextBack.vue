<template>
  <div class="center">
    <button class="btn btn-default back" @click="backUrl">
      <span class="fa fa-backward"/> Назад
    </button>
    <button class="btn btn-default next" @click="nextUrl">Далее
      <span class="fa fa-forward"/>
    </button>
  </div>
</template>

<script>
  export default {
    name: "NextBack",
    props: {
      url: ''
    },
    data() {
      return {
        urls: [
          {url: 'client', component: 'clientView'},
          {url: 'generalInformation', component: 'generalInfo'},
          {url: 'socialBehavior', component: 'socialBehavior'},
          {url: 'chronicDisease', component: 'chronicDisease'},
          {url: 'childList', component: 'childList'},
          {url: 'familyMembers', component: 'familyMembers'},
          {url: 'socialLiving', component: 'socialLivingCondition'},
          {url: 'socialEconomic', component: 'socialEconomicCondition'},
          {url: 'expertOpinion', component: 'expertOpinion'},
        ],
        suburls: [
          {url: 'sourceIncome', component: 'sourceIncome'},
          {url: 'socialPayment', component: 'socialPayment'},
          {url: 'childAllowance', component: 'childAllowance'},
          {url: 'facilities', component: 'facilities'},
        ]
      }
    },
    methods: {
      nextUrl() {
        for (var url in this.urls) {
          if (this.url === this.urls[url].url) {
            if (this.urls.length - 1 !== parseInt(url))
              this.$router.push({name: this.urls[parseInt(url) + 1].component});
          }
        }
        for (var suburl in this.suburls) {
          if (this.url === this.suburls[suburl].url) {
            if (this.suburls.length - 1 !== parseInt(suburl))
              this.$router.push({name: this.suburls[parseInt(suburl) + 1].component});
            else this.$router.push({name: 'expertOpinion'});
          }
        }

        if(this.url === 'husbandInformation') this.$router.push({name: 'socialLivingCondition'});
        if(this.url === 'child' || this.url === 'childAdd') this.$router.push({name: 'familyMembers'});
      },
      backUrl() {
        for (var url in this.urls)
          if (this.url === this.urls[url].url)
            if (0 !== parseInt(url))
              this.$router.push({name: this.urls[parseInt(url) - 1].component});

        for (var suburl in this.suburls) {
          if (this.url === this.suburls[suburl].url) {
            if (0 !== parseInt(suburl))
              this.$router.push({name: this.suburls[parseInt(suburl) - 1].component});
            else this.$router.push({name: 'socialEconomicCondition'});
          }
        }

        if(this.url === 'husbandInformation') this.$router.push({name: 'familyMembers'});
        if(this.url === 'child' || this.url === 'childAdd') this.$router.push({name: 'childList'});
      }
    }
  }
</script>

<style scoped>
  .center {
    text-align: center;
  }

  .btn-default {
    color: #492727;
    font-size: 20px;
    background-color: #D2B48C;
    border-radius: 20px;
  }

  .next {
    margin-left: 10px;
  }

  .back {
    margin-right: 10px;
  }

  .btn-default:hover {
    background-color: #492727;
    color: #D2B48C;
  }
</style>
