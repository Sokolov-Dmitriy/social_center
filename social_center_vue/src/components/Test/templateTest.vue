<template>
  <div>
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
      <next-back v-bind:url="url"></next-back>
    </div>
    <div class="container">
      <button class="btn btn-default noprint" type="button" v-if="!no_data" @click="deleteRequest">УДАЛИТЬ <span
        class="fa fa-trash-o fa-2x"/>
      </button>
      <button class="btn btn-default noprint" type="button" v-if="!no_data" @click="addInfo">РЕДАКТИРОВАТЬ <span
        class="fa fa-pencil fa-2x"/>
      </button>
      <div class="card">
        <div class="card-header">{{ header }}</div>
        <button v-if="!no_data && !isHide" class="btn btn-default noprint" @click="result">Результаты теста
          <span class="fa fa-check-circle"></span>
        </button>
        <table class="table table-hover" v-if="!isHide">
          <thead class="thead noprint">
          <tr>
            <th scope="col">Поле</th>
            <th scope="col">Значение</th>
          </tr>
          </thead>
          <tbody v-for="(value,key) in labels" class="tbody">
          <tr v-if="!['id','client'].includes(key)">
            <td class="td-left">{{ labels[key] }}</td>
            <td>{{ items[key] }}</td>
          </tr>
          </tbody>
        </table>
        <button class="btn btn-default" type="button" v-if="no_data && !isHide" @click="addInfo">ДОБАВИТЬ <span
          class="fa fa-plus-circle fa-2x"/></button>
      </div>
    </div>
  </div>
</template>

<script>
import navBar from "../navBars/navBar";
import sideBarTest from "../Test/sideBarTest";
import sideBar from "../sideBar";
import NextBack from "../Information/NextBack";

export default {
  name: "templateTest",
  components: {
    NextBack,
    sideBar,
    navBar,
    sideBarTest
  },
  props: {
    url: '',
    header: '',
    identifier: '',
    identifier_field: ''
  },
  data() {
    return {
      items: '',
      labels: '',
      no_data: false,
      isHide: false,
      id: '',
      edit: '',
      resultSOCRATES: 0
    }
  },
  created() {
    this.id = this.identifier;
    this.getRequest();
    if (parseInt(this.id) === 0)
      this.addInfo();
  },
  methods: {
    addInfo() {
      this.$emit('addInfo');
      this.isHide = true;
      this.labels = '';
    },
    getRequest() {
      var map = {};
      map[this.identifier_field] = this.id;
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/',
        type: "GET",
        data: map,
        success: (response) => {
          if (response === undefined)
            this.no_data = true;
          else {
            this.id = response.data[0].id;
            this.items = response.data[0].attributes;
            this.labels = response.data[0].attributes.labels;
          }
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
      this.getForPutRequest();
    },
    deleteRequest() {
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.id,
        type: "DELETE",
        success: (response) => {
          this.items = '';
          this.labels = '';
          this.edit = '';
          this.isHide = false;
          this.no_data = true;
          this.$emit('postInfo');
          // alert("Удаление прошло успешно.");
          if (this.url === 'testBoyko') this.$router.push({name: 'testBoykoList'});
          else if (this.url === 'testGAGE') this.$router.push({name: 'testGAGEList'});
          else this.$router.push({name: 'testSOCRATESList'});
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      })
    },
    postRequest(items) {
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/',
        type: "POST",
        data: items,
        success: (response) => {
          // alert("Данные добавлены.");
          this.$emit('postInfo');
          this.isHide = false;
          this.no_data = false;
          this.$emit('newID', response.data.id);
          this.id = response.data.id;
          this.getRequest();
          this.getScore(items, 'post')
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    },
    getForPutRequest() {
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.id,
        type: "GET",
        success: (response) => {
          if (response !== undefined)
            this.edit = response.data[0].attributes;
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    },
    putRequest(items) {
      $.ajax({
        url: this.$store.state.baseUrl + "api/" + this.url + '/' + this.id,
        type: "PUT",
        data: items,
        success: (response) => {
          // alert("Изменение прошло успешно");
          this.$emit('postInfo');
          this.isHide = false;
          this.no_data = false;
          this.getRequest();
          this.getScore(items, 'put')
        },
        error: (response) => {
          if (response.status === 401) this.logOut();
          else alert("Не удалось получить данные с сервера.\nПовторите попытку позже.")
        }
      });
    },
    result() {
      if (this.url === 'testBoyko') this.$router.push({name: 'interpretationBoyko'});
      else if (this.url === 'testGAGE') this.$router.push({name: 'interpretationGAGE'});
      else this.$router.push({name: 'interpretationSOCRATES'});
    },
    getScore(items, type) {
      delete items.client;
      delete items.attempt;
      switch (this.url) {
        case 'testBoyko':
          this.getScoreBoyko(items, type);
          break;
        case 'testGAGE':
          this.getScoreGAGE(items, type);
          break;
        case 'testSOCRATES':
          this.getScoreSOCRATES(items, type);
          break;
      }
    },
    getScoreBoyko(items, type) {
      var result = 0;
      for (let item in items) {
        result += parseInt(items[item]);
        // if ([0, 1].includes(items[item]))
        //   delete items[item];
      }
      items['overall_points'] = result;
      if (result >= 0 && result <= 10)
        items['overall_assessment'] = 0;
      else if (result >= 11 && result <= 20)
        items['overall_assessment'] = 11;
      else if (result >= 21 && result <= 30)
        items['overall_assessment'] = 21;
      else
        items['overall_assessment'] = 31;
      items['test'] = parseInt(this.id);
      if (type === 'post')
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationBoyko/",
          type: "POST",
          data: items,
          success: (response) => {
            // alert("Результат добавлен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
      else
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationBoyko/",
          type: "PUT",
          data: items,
          success: (response) => {
            // alert("Результат изменен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
      // console.log(items['overall_points']);
      // console.log(items['overall_assessment'])
    },
    getScoreGAGE(items, type) {
      var massiv = {};
      var result = 0;
      if (items.alcohol === 0 && items.substances === 0) {
        massiv['risk_abuse'] = 0;
        massiv['overall_points_risk_abuse'] = 0;
        massiv['risk_dependency'] = 0;
        massiv['overall_points_risk_dependency'] = 0;
      } else {
        var fields = ['loss_documents', 'loss_documents_when', 'loss_documents_time', 'do_not_work', 'do_not_work_when',
          'loss_loved_ones', 'fight', 'injuries', 'lots_alcohol', 'lots_alcohol_time', 'drink_alcohol_time', 'try_substances_choice',
          'how_use', 'difficulties', 'poor_health', 'company'];
        // console.log(items)
        for (let item in fields) {
          if (items[fields[item]] !== null && items[fields[item]] !== '')
            result += parseInt(items[fields[item]]);
        }
        if (result >= 3)
          massiv['risk_abuse'] = 3;
        else
          massiv['risk_abuse'] = 0;
        massiv['overall_points_risk_abuse'] = result;
        fields = ['dose_reduction', 'irritation', 'fault', 'tone'];
        result = 0;
        for (let item in fields) {
          if (items[fields[item]] !== null && items[fields[item]] !== '')
            result += parseInt(items[fields[item]]);
        }
        if (result >= 2)
          massiv['risk_dependency'] = 2;
        else
          massiv['risk_dependency'] = 0;
        massiv['overall_points_risk_dependency'] = result;
      }
      massiv['test'] = parseInt(this.id);
      // console.log(massiv);
      if (type === 'post')
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationGAGE/",
          type: "POST",
          data: massiv,
          success: (response) => {
            // alert("Результат добавлен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
      else
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationGAGE/",
          type: "PUT",
          data: massiv,
          success: (response) => {
            // alert("Результат изменен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
    },
    getScoreSOCRATES(items, type) {
      var result = 0;
      var massiv = {};
      for (let item in items) {
        result += parseInt(items[item]);
      }
      if (result >= 19 && result <= 47)
        massiv['ready_change'] = 19;
      else if (result >= 48 && result <= 55)
        massiv['ready_change'] = 48;
      else if (result >= 56 && result <= 77)
        massiv['ready_change'] = 56;
      else if (result >= 78 && result <= 86)
        massiv['ready_change'] = 78;
      else massiv['ready_change'] = 87;
      massiv['overall_points'] = result;
      massiv['realization'] = this.realization(items);
      massiv['overall_points_realization'] = this.resultSOCRATES;
      massiv['ambivalence'] = this.ambivalence(items);
      massiv['overall_points_ambivalence'] = this.resultSOCRATES;
      massiv['action'] = this.action(items);
      massiv['overall_points_action'] = this.resultSOCRATES;
      massiv['test'] = parseInt(this.id);
      if (type === 'post')
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationSOCRATES/",
          type: "POST",
          data: massiv,
          success: (response) => {
            // alert("Результат добавлен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
      else
        $.ajax({
          url: this.$store.state.baseUrl + "api/interpretationSOCRATES/",
          type: "PUT",
          data: massiv,
          success: (response) => {
            // alert("Результат изменен.");
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
            else alert("Не удалось загрузить результаты теста на сервер.\nПовторите попытку позже.")
          }
        });
    },
    realization(items) {
      var result = 0;
      var massiv = ['changes', 'aggravation', 'serious_problem', 'know_trouble', 'much_harm', 'have_problem',
        'alcoholic'];
      for (let item in massiv)
        result += parseInt(items[massiv[item]]);
      this.resultSOCRATES = result;
      if (result >= 7 && result <= 26)
        return 7;
      else if (result >= 27 && result <= 30)
        return 27;
      else if (result >= 31 && result <= 34)
        return 31;
      else return 35;
    },
    ambivalence(items) {
      var result = 0;
      var massiv = ['doubt', 'harm', 'control', 'use_lot'];
      for (let item in massiv)
        result += parseInt(items[massiv[item]]);
      this.resultSOCRATES = result;
      if (result >= 4 && result <= 8)
        return 4;
      else if (result >= 9 && result <= 13)
        return 9;
      else if (result >= 14 && result <= 16)
        return 14;
      else if (result >= 17 && result <= 18)
        return 17;
      else return 19;
    },
    action(items) {
      var result = 0;
      var massiv = ['make_changes', 'too_much', 'changes_lifestyle', 'hold', 'reduce_stop', 'help', 'try_my_best', 'move_on'];
      for (let item in massiv)
        result += parseInt(items[massiv[item]]);
      this.resultSOCRATES = result;
      if (result >= 8 && result <= 25)
        return 8;
      else if (result >= 26 && result <= 30)
        return 26;
      else if (result >= 31 && result <= 35)
        return 31;
      else if (result >= 36 && result <= 38)
        return 36;
      else return 39;
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
  /*border-color: #D2B48C*/
}

.card {
  background-color: #f5eed5;
}

.thead {
  background-color: #D2B48C;
  color: #492727;
}

.table {
  table-layout: fixed;
}

.tbody {
  color: #492727;
  text-align: left;
  border-color: #f5eed5;
}

.btn-default {
  color: #492727;
  font-size: 16px;
}

.btn-default:hover {
  background-color: #E6DFC6;
  color: black;
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

.my-link {
  background-color: #FFF8DC;
  color: #492727;
  font-size: 20px;
  margin-left: 20px;
}

.td-left {
  padding-left: 40px;
}

@media print {
  .noprint {
    display: none;
  }

  .tbody {
    page-break-after: auto;
    page-break-inside: avoid;
    border: none !important;
    margin-bottom: 20px !important;
  }
}

@media only screen and (max-width: 768px) {
  .my-link {
    font-size: 16px;
    margin-left: 0;
  }
}

@media only screen and (max-width: 650px) {
  .my-link {
    font-size: 14px;
    margin-left: 0;
  }
}

@media only screen and (max-width: 540px) {
  .my-link {
    font-size: 12px;
    margin-left: 0;
  }
}

</style>
