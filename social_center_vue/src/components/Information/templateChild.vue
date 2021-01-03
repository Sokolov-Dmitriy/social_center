<template>
  <div>
    <div class="card">
      <div class="card-header" v-html="'2. Сведения о детях'"></div>
      <div v-if="!isHide" class="my-block">2.1. Общая информация</div>
      <table class="table table-hover" v-if="!isHide">
        <!--        <thead class="thead noprint" v-if="end">-->
        <!--        <tr>-->
        <!--          <th scope="col">Поле</th>-->
        <!--          <th scope="col">Значение</th>-->
        <!--        </tr>-->
        <!--        </thead>-->
        <tbody v-for="(value,key) in label_first" class="tbody">
        <tr>
          <td class="td-left">{{ label_first[key] }}</td>
          <td>{{ first[key] }}</td>
        </tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <div v-if="!isHide" class="card-header" v-html="'2. Сведения о детях'"></div>
      <div v-if="!isHide" class="my-block">2.2. Информация о состоянии здоровья ребёнка</div>
      <table class="table table-hover" v-if="!isHide">
        <!--        <thead class="thead noprint" v-if="end">-->
        <!--        <tr>-->
        <!--          <th scope="col">Поле</th>-->
        <!--          <th scope="col">Значение</th>-->
        <!--        </tr>-->
        <!--        </thead>-->
        <tbody v-for="(value,key) in label_second" class="tbody">
        <tr>
          <td class="td-left">{{ label_second[key] }}</td>
          <td>{{ second[key] }}</td>
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
@import "../../assets/css/view-style.css";
</style>
