<template>
  <div>
    <button v-if="component" class="btn btn-default" @click="nextStep">{{header}}
      <span class="fa fa-plus-circle"></span>
      <span class="fa fa-pencil"></span>
    </button>
    <b-form-select v-if="options" :options="options" v-model="component" @change="nextStep"></b-form-select>
  </div>
</template>

<script>
  export default {
    name: "navigation",
    props: {
      url: '',
      id: ''
    },
    data() {
      return {
        header: '',
        component: '',
        options: '',
      }
    },
    created() {
      if (this.url === 'familyMembers') {
        this.header = '3.2 Информация о муже/партнёре';
        this.component = 'husbandInformation';
      } else if (this.url === 'socialEconomic') {
        this.options = [
          {text: 'Выберите следующие подпункты:', value: ''},
          {text: 'Источники дохода', value: 'sourceIncome'},
          {text: 'Социальны выплаты', value: 'socialPayment'},
          {text: 'Детские пособия и компенсационные выплаты', value: 'childAllowance'},
          {text: 'Льготы и меры социальной поддержки, предусмотренные для определённых категорий', value: 'facilities'},
        ];
      }
    },
    methods: {
      nextStep() {
        // if (!['familyMembers', 'socialEconomic'].includes(this.url))
        //   this.$router.push({name: this.component});
        this.$router.push({name: this.component, params: {id: this.id}});
      }
    }
  }
</script>

<style scoped>
  .btn-default {
    color: #492727;
    font-size: 16px;
  }

  .btn-default:hover {
    background-color: #E6DFC6;
    color: black;
  }

  select {
    background-color: #f5eed5;
    color: #492727;
  }

  select:hover {
    background-color: #E6DFC6;
    color: black;
  }
</style>
