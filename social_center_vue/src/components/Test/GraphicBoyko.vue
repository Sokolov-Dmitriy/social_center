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
      <next-back v-bind:url="'graphicBoyko'"></next-back>
    </div>
    <div class="container">
      <div class="card">
        <div class="card-header">Результаты тестов клиента по методике Бойко Е.О.</div>
        <div class="subtitle">{{ this.dates.date1.text }}: {{ this.dates.date1.date }} {{ this.dates.date1.time }}</div>
        <div class="subtitle">{{ this.dates.date2.text }}: {{ this.dates.date2.date }} {{ this.dates.date2.time }}</div>
        <horizontal v-if="gotChart" :chart-data="chartdata" :options="options" class="chart-container"></horizontal>
        <horizontal v-if="gotChart" :chart-data="chartdata2" :options="options2" class="chart-container2"></horizontal>
      </div>
    </div>
    <MainFooter v-if="gotChart" class="noprint"></MainFooter>
  </div>
</template>

<script>
import Horizontal from "./Horizontal";
import sideBarTest from "./sideBarTest";
import sideBar from "../sideBar";
import navBar from "../navBars/navBar";
import NextBack from "../Information/NextBack";
import MainFooter from "../footers/MainFooter";

export default {
  name: "GraphicBoyko",
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
    var date = '';
    $.ajax({
      url: this.$store.state.baseUrl + "api/graphicBoyko/",
      type: "GET",
      data: {client: parseInt(sessionStorage.getItem('id'))},
      success: (response) => {
        this.items = response.data.data;
        this.labels = response.data.labels;
        for (let test in this.items) {
          if (this.items[test].attempt === 1) {
            this.test_1 = this.items[test];
          } else if (this.items[test].attempt === 2) {
            this.test_2 = this.items[test];
          }
        }
        for (let item in response.data.date)
          if (response.data.date[item].attempt === 1) {
            date = new Date(response.data.date[item].date);
            this.dates.date1.date = date.toLocaleDateString('ru');
            this.dates.date1.time = date.toLocaleTimeString('ru');
          } else {
            date = new Date(response.data.date[item].date);
            this.dates.date2.date = date.toLocaleDateString('ru');
            this.dates.date2.time = date.toLocaleTimeString('ru');
          }
        // console.log(this.test_1, this.test_2);
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
      var result = 0;
      var result2 = 0;
      for (var value in this.test_1) {
        if (['attempt', 'client', 'id'].includes(value)) {
          delete this.test_1[value];
          delete this.test_2[value];
        } else {
          result += this.test_1[value];
          result2 += this.test_2[value];
        }
      }
      // console.log(this.test_1, this.test_2,result,result2);
      delete this.labels['overall_points'];
      delete this.labels['overall_assessment'];
      delete this.labels['date'];
      this.labels['criticism'] = ['Способность критически воспринимать', 'свое состояние и поведение'];
      this.chartdata.datasets[0].data = Object.values(this.test_1);
      this.chartdata.datasets[1].data = Object.values(this.test_2);
      this.chartdata.labels = Object.values(this.labels);
      this.chartdata2.datasets[0].data.push(result);
      this.chartdata2.datasets[1].data.push(result2);
      this.gotChart = true;
    }
  }
}
</script>

<style scoped>
@import "../../assets/css/graphic-style.css";
</style>
