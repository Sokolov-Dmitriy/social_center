<template>
  <div>
    <div class="noprint">
      <nav-bar></nav-bar>
      <button class="btn btn-default" type="button" v-b-toggle.sidebar-border>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <b-link to="/info" class="my-link">Общие сведения</b-link>
      <button class="btn btn-default-right" type="button" v-b-toggle.sidebar-test>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <side-bar-test></side-bar-test>
      <side-bar></side-bar>
      <next-back v-bind:url="'graphicSOCRATES'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Результаты тестов клиента по методике SOCRATES</div>
        <div class="subtitle">{{this.dates.date1.text}}: {{this.dates.date1.date}} {{this.dates.date1.time}}</div>
        <div class="subtitle">{{this.dates.date2.text}}: {{this.dates.date2.date}} {{this.dates.date2.time}}</div>
        <horizontal v-if="gotChart" :chart-data="chartdata" :options="options" class="chart-container"></horizontal>
        <horizontal v-if="gotChart" :chart-data="chartdata2" :options="options2" class="chart-container2"></horizontal>
      </div>
    </div>
  </div>
</template>

<script>
  import sideBarTest from "./sideBarTest";
  import sideBar from "../sideBar";
  import navBar from "../navBar";
  import Horizontal from "./Horizontal";
  import NextBack from "../Information/NextBack";

  export default {
    name: "GraphicSOCRATES",
    components: {
      NextBack,
      sideBarTest,
      sideBar,
      navBar,
      Horizontal
    },
    data() {
      return {
        dates: {
          date1: {
            date: '',
            time: '',
            text: 'Первичная диагностика'
          },
          date2: {
            date: '',
            time: '',
            text: 'Вторичная диагностика'
          },
        },
        items: '',
        labels: '',
        test_1: '',
        test_2: '',
        gotChart: false,
        chartdata: {
          labels: [],
          datasets: [{
            label: 'Первичная диагностика',
            backgroundColor: 'darkblue',
            data: []
          },
            {
              label: 'Вторичная диагностика',
              backgroundColor: 'purple',
              data: []
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            datalabels: {
              color: 'white',
              font: {
                weight: 'bold'
              },
              formatter: function (value, context) {
                return value;
              }
            }
          },
          scales: {
            xAxes: [
              {
                ticks: {
                  min: 1,
                  max: 40,
                },
              },
            ],
          },
        },
        chartdata2: {
          labels: [],
          datasets: [{
            label: 'Первичная диагностика',
            backgroundColor: 'darkblue',
            data: []
          },
            {
              label: 'Вторичная диагностика',
              backgroundColor: 'purple',
              data: []
            }
          ]
        },
        options2: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            datalabels: {
              color: 'white',
              font: {
                weight: 'bold'
              },
              formatter: function (value, context) {
                return value;
              }
            }
          },
          scales: {
            xAxes: [
              {
                ticks: {
                  min: 1,
                  max: 95,
                },
              },
            ],
          },
        }
      }
    },
    created() {
      var date = '';
      $.ajax({
        url: this.$store.state.baseUrl+"api/graphicSOCRATES/",
        type: "GET",
        data: {client: parseInt(sessionStorage.getItem('id'))},
        success: (response) => {
          // console.log(response)
          this.items = response.data.data;
          this.labels = response.data.labels;
          for (let test in this.items) {
            if (this.items[test].attempt === 1) {
              this.test_1 = this.items[test].test[0];
              date = new Date(this.items[test].test[0].date);
              this.dates.date1.date = date.toLocaleDateString('ru');
              this.dates.date1.time = date.toLocaleTimeString('ru');
            } else if (this.items[test].attempt === 2) {
              this.test_2 = this.items[test].test[0];
              date = new Date(this.items[test].test[0].date);
              this.dates.date2.date = date.toLocaleDateString('ru');
              this.dates.date2.time = date.toLocaleTimeString('ru');
            }
          }
          this.graphic()
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    }
    ,
    methods: {
      graphic() {
        var result1 = this.test_1.overall_points;
        var result2 = this.test_2.overall_points;
        var label = this.labels.ready_change;
        for (var item in this.test_1)
          if (!['overall_points_realization', 'overall_points_ambivalence', 'overall_points_action'].includes(item)) {
            delete this.test_1[item];
            delete this.test_2[item];
          } else delete this.labels[item];
        delete this.labels['overall_points'];
        delete this.labels['ready_change'];
        delete this.labels['date'];
        this.chartdata.labels = Object.values(this.labels);
        this.chartdata.datasets[0].data = Object.values(this.test_1);
        this.chartdata.datasets[1].data = Object.values(this.test_2);
        this.chartdata2.labels.push(label);
        this.chartdata2.datasets[0].data.push(result1);
        this.chartdata2.datasets[1].data.push(result2);
        this.gotChart = true;
      }
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 2%;
    text-align: center;
  }

  .card-header {
    display: block;
    font-size: 30px;
    font-weight: 700;
    padding: 30px 0;
    color: #492727;
    background-color: #D2B48C;
  }

  .card {
    background-color: #f5eed5;
  }

  .my-link {
    background-color: #FFF8DC;
    color: #492727;
    font-size: 20px;
    margin-left: 20px;
  }

  .btn-default:hover {
    background-color: #E6DFC6;
    color: black;
  }

  .btn-default {
    color: #492727;
    font-size: 16px;
  }

  .btn-default-right {
    float: right;
    color: #492727;
    font-size: 16px;
  }

  .btn-default-right:hover {
    background-color: #E6DFC6;
    color: black;
  }

  .chart-container {
    width: 85% !important;
    margin: 0 auto 20px;
  }

  .chart-container2 {
    width: 85% !important;
    height: 200px;
    margin: 0 auto 20px;
  }

  .subtitle {
    display: block;
    font-size: 20px;
    font-weight: 600;
    padding: 20px 0;
    color: #492727;
    background-color: #D2B48C;
  }

  @media print {
    .noprint {
      display: none;
    }

    .chart-container {
      min-height: 100%;
      max-width: 100%;
      max-height: 100%;
      height: auto !important;
      width: auto !important;
    }

    .chart-container2 {
      min-height: 100%;
      max-width: 100%;
      max-height: 100%;
      height: auto !important;
      width: auto !important;
    }
  }
</style>
