<template>
  <div class="chart">
    <div v-for="chart in chartsData.simple">
      <div style="margin-right: 20px; margin-left: 20px; margin-top: 10px; margin-bottom: 10px;">

        <p class="h3 text-center">{{chart.chartData.labelMe}}</p>
        <horizontal v-bind:style="'height:'+chart.chartData.heightMy+'px;'" v-if="gotChart"
                    :chart-data="chart.chartData" :options="chart.options"
                    class="chart-container"></horizontal>
      </div>
    </div>
    <div v-if="chartsData.childs.length!=0">
      <br>
      <p class="h2 text-center">Информация о детях</p>
      <br>
      <div v-for="chart in chartsData.childs">
        <div style="margin-right: 20px; margin-left: 20px; margin-top: 10px; margin-bottom: 10px;">

          <p class="h3 text-center">{{chart.chartData.labelMe}}</p>
          <horizontal v-bind:style="'height:'+chart.chartData.heightMy+'px;'" v-if="gotChart"
                      :chart-data="chart.chartData" :options="chart.options"
                      class="chart-container"></horizontal>
        </div>
      </div>
    </div>
    <div v-for="chart in chartsData.tests">
      <div style="margin-right: 20px; margin-left: 20px; margin-top: 10px; margin-bottom: 10px;">

        <p class="h3 text-center">{{chart.inter.chartData.labelMe}}</p>
        <horizontal v-bind:style="'height:'+chart.inter.chartData.heightMy+'px;'" v-if="gotChart"
                    :chart-data="chart.inter.chartData" :options="chart.inter.options"
                    class="chart-container"></horizontal>
        <p class="h4 text-center">{{chart.fullBalls.chartData.labelMe}}</p>
        <div style="height: 100px;">
          <horizontal style="height: 100px;" v-if="gotChart" :chart-data="chart.fullBalls.chartData"
                      :options="chart.fullBalls.options"
                      class="chart-container2"></horizontal>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Horizontal from "../Test/Horizontal";

  export default {
    name: 'CountingMenu',
    components: {
      Horizontal
    },
    props: ['chartDat', 'gotChart'],
    data() {
      return {
        chartsData: this.chartDat,
      }
    }
  }
</script>

<style scoped>
  .chart {
    margin-top: 120px;

  }
</style>
