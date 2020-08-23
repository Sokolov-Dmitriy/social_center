<template>
  <div>
    <div class="card">
      <div class="card-header" v-html="'2.1. Общая информация'"></div>
      <table class="table table-hover" v-if="!isHide">
        <thead class="thead noprint" v-if="end">
        <tr>
          <th scope="col">Поле</th>
          <th scope="col">Значение</th>
        </tr>
        </thead>
        <tbody v-for="(value,key) in label_first" class="tbody">
        <tr>
          <td>{{label_first[key]}}</td>
          <td>{{first[key]}}</td>
        </tr>
        </tbody>
      </table>
    </div>

  <div class="card">
    <div class="card-header" v-html="'2.2. Информация о состоянии здоровья ребёнка'" v-if="!isHide"></div>
    <table class="table table-hover">
      <thead class="thead noprint" v-if="end">
      <tr>
        <th scope="col">Поле</th>
        <th scope="col">Значение</th>
      </tr>
      </thead>
      <tbody v-for="(value,key) in label_second" class="tbody">
      <tr>
        <td>{{label_second[key]}}</td>
        <td>{{second[key]}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
  export default {
    name: "templateChild",
    props: {
      no_data: false,
      isHide: false
    },
    data() {
      return {
        first: {},
        second: {},
        label_first: {},
        label_second: {},
        end: false
      }
    },
    methods: {
      slice(items, labels) {
        var array = ['health', 'withdrawal_symptoms', 'with_mother',
          'hiv_status_child', 'hiv_plus', 'center_aids', 'center_prevention', 'hiv_prevention'];
        delete items['labels'];
        delete labels['id'];
        delete labels['client'];
        for (var item in items)
          if (array.includes(item)) {
            this.second[item] = items[item];
            this.label_second[item] = labels[item];
            delete items[item];
            delete labels[item]
          }
        this.label_first = labels;
        this.first = items;
        this.end = true
      },
    }
  }
</script>

<style scoped>
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

  .thead {
    background-color: #D2B48C;
    color: #492727;
  }

  .table {
    table-layout: fixed;
  }

  .tbody {
    color: #492727;
    text-align: center;
    border-color: #f5eed5;
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
</style>
