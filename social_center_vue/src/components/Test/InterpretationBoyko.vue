<template>
  <div class="general">
    <div class="noprint">
      <nav-bar></nav-bar>
      <button class="btn btn-default" type="button" v-b-toggle.sidebar-border>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <b-link to="/info" class="my-link">{{ this.$store.state.fullName }}</b-link>
      <button class="btn btn-default-right" type="button" v-b-toggle.sidebar-test>
        <span class="fa fa-bars fa-2x" style="color:#492727;"></span>
      </button>
      <side-bar-test></side-bar-test>
      <side-bar></side-bar>
      <next-back v-bind:url="'interpretationBoyko'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Результаты по методике Бойко Е.О.</div>
        <div class="subtitle">{{ this.date.text }}: {{ this.date.date }} {{ this.date.time }}</div>
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
          <tr v-if="!['id','test','overall_points'].includes(key)">
            <td class="green-td" v-if="items[key]==='проблемы не выявлены'">{{ labels[key] }}</td>
            <td v-else-if="key==='overall_assessment'">{{ labels[key] }}</td>
            <td v-else class="red-td">{{ labels[key] }}</td>
            <td class="green-td" v-if="items[key]==='проблемы не выявлены'">{{ items[key] }}</td>
            <td v-else-if="key==='overall_assessment'">{{ items[key] }}</td>
            <td v-else class="red-td">{{ items[key] }}</td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <MainFooter v-if="gotChart" class="noprint"></MainFooter>
  </div>
</template>

<script>
import sideBarTest from "./sideBarTest";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import ChartDataLabels from 'chartjs-plugin-datalabels';
// import {HorizontalBar} from "vue-chartjs";

import Horizontal from "./Horizontal";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "InterpretationBoyko",
  components: {
    NextBack,
    sideBarTest,
    sideBar,
    navBar,
    Horizontal,
    MainFooter
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
                min: 0,
                max: 4,
                stepSize: 1
              },
            },
          ],
        },
      },
      chartdata2: {
        labels: [['Общая оценка', 'социального', 'функционирования']],
        datasets: [{
          label: 'Баллы',
          backgroundColor: 'blue',
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
                min: 0,
                max: 40,
                stepSize: 1
              },
            },
          ],
        },
      }
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/interpretationBoyko/",
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
  },
  methods: {
    getChartLabel() {
      var array = [];
      for (var label in this.labels)
        if (!['id', 'test', 'overall_points', 'overall_assessment'].includes(label))
          if (label === 'criticism')
            array.push(['Способность критически воспринимать', 'свое состояние и поведение']);
          else array.push(this.labels[label]);
      this.chartdata.labels = array;

      $.ajax({
        url: this.$store.state.baseUrl + "api/testBoyko/" + sessionStorage.getItem('id_test'),
        type: "GET",
        success: (response) => {
          var colors = [];
          var result = 0;
          var values = response.data[0].attributes;
          for (var value in values) {
            if (value === 'attempt')
              delete values[value];
            else {
              colors.push(this.getColor(values[value]));
              result += values[value]
            }
          }
          // console.log(values, colors, result);
          this.chartdata.datasets[0].data = Object.values(values);
          this.chartdata.datasets[0].backgroundColor = colors;
          this.chartdata2.datasets[0].data.push(result);
          this.gotChart = true;
        },
        error: (response) => {
          alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    },
    getColor(value) {
      if ([0, 1].includes(value)) return 'green';
      else return 'darkred';
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/graphic-style.css";

.thead {
  background-color: #D2B48C;
  color: #492727;
}

.tbody {
  color: #492727;
  text-align: left;
  border-color: #f5eed5;
}

.green-td {
  color: green;
}

.red-td {
  color: darkred;
}

.chart-container2 {
  height: 100px;
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
  .tbody {
    page-break-after: auto;
    page-break-inside: avoid;
    border: none !important;
    margin-bottom: 20px !important;
  }
}
</style>
