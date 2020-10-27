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
    url: '',
  },
  data() {
    return {
      urls: [
        {url: 'client', component: 'clientView'},
        {url: 'socialBehavior', component: 'socialBehavior'},
        {url: 'chronicDisease', component: 'chronicDisease'},
        {url: 'childList', component: 'childList'},
        {url: 'familyMembers', component: 'familyMembers'},
        {url: 'husbandList', component: 'husbandList'},
        {url: 'socialLiving', component: 'socialLivingCondition'},
        {url: 'socialEconomic', component: 'socialEconomicCondition'},
        {url: 'expertOpinion', component: 'expertOpinion'},
      ],
      suburls: [
        {url: 'sourceIncome', component: 'sourceIncome'},
        {url: 'socialPayment', component: 'socialPayment'},
        {url: 'childAllowance', component: 'childAllowance'},
        {url: 'facilities', component: 'facilities'},
      ],
      testurls: [
        {url: 'testBoykoList', component: 'testBoykoList'},
        {url: 'testGAGEList', component: 'testGAGEList'},
        {url: 'testSOCRATESList', component: 'testSOCRATESList'},
        {url: 'typologicalGroupList', component: 'typologicalGroupList'},
      ],
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

      if (this.url === 'child' || this.url === 'childAdd') this.$router.push({name: 'familyMembers'});
      if (this.url === 'husbandInformation' || this.url === 'husbandAdd') this.$router.push({name: 'socialLivingCondition'});

      for (var testurl in this.testurls) {
        if (this.url === this.testurls[testurl].url) {
          if (this.testurls.length - 1 !== parseInt(testurl))
            this.$router.push({name: this.testurls[parseInt(testurl) + 1].component});
        }
      }

      if (['graphicBoyko', 'testBoyko', 'interpretationBoyko'].includes(this.url)) this.$router.push({name: 'testGAGEList'});
      if (['graphicGAGE', 'testGAGE', 'interpretationGAGE'].includes(this.url)) this.$router.push({name: 'testSOCRATESList'});
      if (['graphicSOCRATES', 'testSOCRATES', 'interpretationSOCRATES'].includes(this.url)) this.$router.push({name: 'typologicalGroupList'});
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

      if (this.url === 'child' || this.url === 'childAdd') this.$router.push({name: 'childList'});
      if (this.url === 'husbandInformation' || this.url === 'husbandAdd') this.$router.push({name: 'husbandList'});

      for (var testurl in this.testurls) {
        if (this.url === this.testurls[testurl].url) {
          if (0 !== parseInt(testurl))
            this.$router.push({name: this.testurls[parseInt(testurl) - 1].component});
        }
      }

      if (['graphicBoyko', 'testBoyko'].includes(this.url)) this.$router.push({name: 'testBoykoList'});
      if (['graphicGAGE', 'testGAGE'].includes(this.url)) this.$router.push({name: 'testGAGEList'});
      if (['graphicSOCRATES', 'testSOCRATES'].includes(this.url)) this.$router.push({name: 'testSOCRATESList'});

      if (this.url === 'interpretationBoyko') this.$router.push({name: 'testBoyko'});
      if (this.url === 'interpretationGAGE') this.$router.push({name: 'testGAGE'});
      if (this.url === 'interpretationSOCRATES') this.$router.push({name: 'testSOCRATES'});

      if (this.url === 'typologicalGroup') this.$router.push({name: 'typologicalGroupList'});
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
