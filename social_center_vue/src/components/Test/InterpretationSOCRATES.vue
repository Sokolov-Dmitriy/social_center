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
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Результаты по методике SOCRATES</div>
        <div class="subtitle">{{this.date.text}}: {{this.date.date}} {{this.date.time}}</div>
        <horizontal v-if="gotChart" :chart-data="chartdata" :options="options" class="chart-container"></horizontal>
        <horizontal v-if="gotChart" :chart-data="chartdata2" :options="options2" class="chart-container2"></horizontal>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Шкалы</th>
            <th scope="col">Интерпретация</th>
          </tr>
          </thead>
          <tbody class="tbody" v-for="(value,key) in labels">
          <tr v-if="!['id','test','overall_points','overall_points_realization','overall_points_ambivalence',
                'overall_points_action'].includes(key)">
            <td>{{labels[key]}}</td>
            <td>{{items[key]}}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
  import sideBarTest from "./sideBarTest";
  import sideBar from "../sideBar";
  import navBar from "../navBar";
  import Horizontal from "./Horizontal";

  export default {
    name: "InterpretationSOCRATES",
    components: {
      sideBarTest,
      sideBar,
      navBar,
      Horizontal
    },
    data() {
      return {
        date: {
          date: '',
          time: '',
          text: ''
        },
        gotChart: false,
        items: '',
        labels: '',
        chartdata: {
          labels: [],
          datasets: [{
            label: 'Баллы',
            backgroundColor: 'blue',
            data: []
          }
          ]
        },
        options: {
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
                  // stepSize: 1
                },
              },
            ],
          },
        },
        chartdata2: {
          labels: [],
          datasets: [{
            label: 'Баллы',
            backgroundColor: 'blue',
            data: []
          }
          ]
        },
        options2: {
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
                  // stepSize: 1
                },
              },
            ],
          },
        }
      }
    },
    created() {
      $.ajax({
        url: this.$store.state.baseUrl+"api/interpretationSOCRATES/",
        type: "GET",
        data: {test: parseInt(sessionStorage.getItem('id_test'))},
        success: (response) => {
          this.items = response.data[0].attributes;
          this.labels = response.data[0].attributes.labels;
          this.date.text = response.data[0].attributes.labels.date;
          var date = new Date(response.data[0].attributes.date);
          this.date.date = date.toLocaleDateString('ru');
          this.date.time = date.toLocaleTimeString('ru');
          delete this.items['date'];
          delete this.labels['date'];
          this.getChartLabel()
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    }
    ,
    methods: {
      getChartLabel() {
        var array = [];
        for (var label in this.labels)
          if (!['id', 'test', 'overall_points', 'overall_points_action', 'overall_points_ambivalence',
            'overall_points_realization', 'ready_change', 'date'].includes(label))
            array.push(this.labels[label]);
        this.chartdata.labels = array;
        this.chartdata.datasets[0].data = [this.items['overall_points_realization'],
          this.items['overall_points_ambivalence'], this.items['overall_points_action']];

        this.chartdata2.labels.push(this.labels['ready_change']);
        this.chartdata2.datasets[0].data.push(this.items['overall_points']);
        // console.log(this.items);
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

  .card-header {
    display: block;
    font-size: 30px;
    font-weight: 700;
    padding: 30px 0;
    color: #492727;
    background-color: #D2B48C;
    /*border-color: #D2B48C*/
  }

  .card {
    background-color: #f5eed5;
  }

  .thead {
    background-color: #D2B48C;
    color: #492727;
  }

  .tbody {
    color: #492727;
    text-align: left;
    border-color: #f5eed5;
  }

  .big-td {
    font-weight: bolder;
  }

  .chart-container {
    width: 85% !important;
    margin: 0 auto;
  }

  .chart-container2 {
    width: 85% !important;
    height: 100px;
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

    .tbody {
      page-break-after: auto;
      page-break-inside: avoid;
      border: none !important;
      margin-bottom: 20px !important;
    }
  }
</style>
