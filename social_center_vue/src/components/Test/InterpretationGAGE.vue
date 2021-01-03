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
      <next-back v-bind:url="'interpretationGAGE'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Результаты по методике GAGE</div>
        <div class="subtitle">{{ this.date.text }}: {{ this.date.date }} {{ this.date.time }}</div>
        <horizontal v-if="gotChart" :chart-data="chartdata" :options="options" class="chart-container"></horizontal>
        <table class="table table-hover">
          <thead class="thead">
          <tr>
            <th scope="col">Шкалы</th>
            <th scope="col">Интерпретация</th>
          </tr>
          </thead>
          <tbody class="tbody" v-for="(value,key) in labels">
          <tr v-if="!['id','test','overall_points_risk_abuse','overall_points_risk_dependency'].includes(key)">
            <td class="green-td" v-if="items[key]==='проблемы не выявлены'">{{ labels[key] }}</td>
            <td v-else class="red-td">{{ labels[key] }}</td>
            <td class="green-td" v-if="items[key]==='проблемы не выявлены'">{{ items[key] }}</td>
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
import Horizontal from "./Horizontal";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "InterpretationGAGE",
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
          backgroundColor: [],
          data: []
        }
        ]
      },
      options: {
        maintainAspectRatio: false,
        // responsive: false,
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
                max: 28,
                stepSize: 1,
              },
            },
          ],
        },
      }
    }
  },
  created() {
    $.ajax({
      url: this.$store.state.baseUrl + "api/interpretationGAGE/",
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
      var colors = [];
      for (var label in this.labels) {
        if (!['id', 'test', 'overall_points_risk_abuse', 'overall_points_risk_dependency'].includes(label))
          array.push(this.labels[label]);
        if (label === 'overall_points_risk_abuse') {
          if (this.items[label] >= 3) colors.push('darkred');
          else colors.push('green')
        }
        if (label === 'overall_points_risk_dependency') {
          if (this.items[label] >= 2) colors.push('darkred');
          else colors.push('green')
        }
      }
      this.chartdata.labels = array;
      this.chartdata.datasets[0].data = [this.items['overall_points_risk_abuse'],
        this.items['overall_points_risk_dependency']];
      this.chartdata.datasets[0].backgroundColor = colors;
      this.gotChart = true;
    },
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

@media print {

  .tbody {
    page-break-after: auto;
    page-break-inside: avoid;
    border: none !important;
    margin-bottom: 20px !important;
  }
}
</style>
