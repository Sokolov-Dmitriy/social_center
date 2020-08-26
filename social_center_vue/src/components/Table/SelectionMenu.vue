<template>
  <div class="container">
    <span class="heading">Выберите пункты для формирования таблицы</span>
    <div class="checkboxes">
      <b-form-checkbox class="checkbox" id="0" v-model="checkValue[0]" v-on:change="chooseAll(checkValue[0])"
                       v-bind:checked="checkValue[0]">Выбрать все
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-model="checkValue[1]"
                       v-bind:checked="checkValue[1]">Сведения о клиенте(общее)
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" id="1" v-on:change="setChoose(checkValue[2],3,5)"
                       v-model="checkValue[2]" v-bind:checked="checkValue[2]">1. Сведения о клиенте
        <i class="fa fa-sort-desc" aria-hidden="true" v-if="hide1===false" @click="hideFirstBlock"></i>
        <i class="fa fa-caret-right" aria-hidden="true" v-if="hide1===true" @click="hideFirstBlock"></i>
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <div class="div-my" v-bind:hidden="hide1">
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[3],2)"
                         v-model="checkValue[3]"
                         v-bind:checked="checkValue[3]">1.1. Общая информация
        </b-form-checkbox>
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[4],2)"
                         v-model="checkValue[4]"
                         v-bind:checked="checkValue[4]">1.2. Информация о противоправных действиях, правонарушениях,
          употреблении наркотиков, алкоголя
        </b-form-checkbox>
        <b-form-checkbox class="checkbox" type="checkbox" v-on:change="setFalse(checkValue[5],2)"
                         v-model="checkValue[5]" v-bind:checked="checkValue[5]">1.3. Информация о наличии хронического
          заболевания
        </b-form-checkbox>
      </div>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-bind:checked="checkValue[6]" v-model="checkValue[6]">
        2. Сведения о детях
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-on:change="setChoose(checkValue[7],8,9)"
                       v-model="checkValue[7]" v-bind:checked="checkValue[7]">3. Сведения о членах семьи
        <i class="fa fa-sort-desc" aria-hidden="true" v-if="hide2===false" @click="hideSecondBlock"></i>
        <i class="fa fa-caret-right" aria-hidden="true" v-if="hide2===true" @click="hideSecondBlock"></i>
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <div class="div-my" v-bind:hidden="hide2">
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[8],7)" v-model="checkValue[8]"
                         v-bind:checked="checkValue[8]">3.1. Общие сведения
        </b-form-checkbox>
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[9],7)" v-model="checkValue[9]"
                         v-bind:checked="checkValue[9]">3.2. Информация о
          муже/партнёре
        </b-form-checkbox>
      </div>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-on:change="setChoose(checkValue[10],11,12)" v-model="checkValue[10]"
                       v-bind:checked="checkValue[10]">4. Сведения о социально-бытовом и
        социально-экономическом положении
        <i class="fa fa-sort-desc" aria-hidden="true" v-if="hide3===false" @click="hideThirdBlock"></i>
        <i class="fa fa-caret-right" aria-hidden="true" v-if="hide3===true" @click="hideThirdBlock"></i>
      </b-form-checkbox>
    </div>

    <div class="checkboxes">
      <div class="div-my" v-bind:hidden="hide3">
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[11],10)"
                         v-model="checkValue[11]" v-bind:checked="checkValue[11]">4.1. Социально-бытовые условия
        </b-form-checkbox>
        <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[12],10)" v-model="checkValue[12]"
                         v-bind:checked="checkValue[12]">
          4.2. Социально-экономические условия проживания
        </b-form-checkbox>
      </div>
    </div>

    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-bind:checked="checkValue[13]" v-model="checkValue[13]">5. Заключение
        специалиста
      </b-form-checkbox>
    </div>

    <!--      занесение тестов -->
    <div class="checkboxes">
      <b-form-checkbox class="checkbox" v-on:change="setChoose(checkValue[14],15,22)" v-model="checkValue[14]"
                       v-bind:checked="checkValue[14]">6.Тесты
        <i class="fa fa-sort-desc" aria-hidden="true" v-if="hide4===false" @click="hide4Block"></i>
        <i class="fa fa-caret-right" aria-hidden="true" v-if="hide4===true" @click="hide4Block"></i></b-form-checkbox>
    </div>
    <div class="checkboxes">
      <div class="div-my" v-bind:hidden="hide4">
        <b-form-checkbox class="checkbox" v-on:change="setChoose(checkValue[15],16,18)"
                         v-model="checkValue[15]" v-bind:checked="checkValue[15]">Первичная диагностика
          <i class="fa fa-sort-desc" aria-hidden="true" v-if="hide5===false" @click="hide5Block"></i>
          <i class="fa fa-caret-right" aria-hidden="true" v-if="hide5===true" @click="hide5Block"></i></b-form-checkbox>
        <div class="div-my" v-bind:hidden="hide5">
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[16],15)"
                           v-model="checkValue[16]" v-bind:checked="checkValue[16]">Бойко
          </b-form-checkbox>
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[17],15)" v-model="checkValue[17]"
                           v-bind:checked="checkValue[17]">GAGE
          </b-form-checkbox>
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[18],15)" v-model="checkValue[18]"
                           v-bind:checked="checkValue[18]">SOCRATES
          </b-form-checkbox>
        </div>
        <b-form-checkbox class="checkbox" v-on:change="setChoose(checkValue[19],20,22)"
                         v-model="checkValue[19]" v-bind:checked="checkValue[19]">Вторичная диагностика
          <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide6===false" @click="hide6Block"></i>
          <i class="fa fa-caret-right" aria-hidden="true" v-if="hide6===true" @click="hide6Block"></i></b-form-checkbox>
        <div class="div-my" v-bind:hidden="hide6">
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[20],19)"
                           v-model="checkValue[20]" v-bind:checked="checkValue[20]">Бойко
          </b-form-checkbox>
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[21],19)" v-model="checkValue[21]"
                           v-bind:checked="checkValue[21]">GAGE
          </b-form-checkbox>
          <b-form-checkbox class="checkbox" v-on:change="setFalse(checkValue[22],19)" v-model="checkValue[22]"
                           v-bind:checked="checkValue[22]">SOCRATES
          </b-form-checkbox>
        </div>
      </div>
    </div>

    <button type="button" class="btn btn-primary" v-on:click="chooseChecked">Сформировать таблицу</button>
  </div>

</template>

<script>
  // import $ from "jquery";

  export default {
    name: "SelectionMenu",
    data() {
      return {
        hide1: true,
        hide2: true,
        hide3: true,
        hide4: true,
        hide5: true,
        hide6: true,
        checkValue: [],
      }
    },
    methods: {
      hideFirstBlock() {
        this.hide1 = !this.hide1;
      },
      hideSecondBlock() {
        this.hide2 = !this.hide2;
      },
      hideThirdBlock() {
        this.hide3 = !this.hide3;
      },
      hide4Block() {
        this.hide4 = !this.hide4;
      },
      hide5Block() {
        this.hide5 = !this.hide5;
      },
      hide6Block() {
        this.hide6 = !this.hide6;
      },
      initArray() {
        console.log("init");
        for (let i = 0; i < 23; i++) {
          this.checkValue.push(false);
        }
      },
      chooseAll(signal) {
        for (let i = 0; i < 23; i++) {
          this.checkValue[i] = !signal;
        }
      },
      setChoose(signal, start, end) {
        for (let i = start; i < end + 1; i++) {
          this.checkValue[i] = !signal;
        }
      },
      setFalse(signal, secondPoint) {
        if (signal) {
          this.checkValue[0] = false;
          this.checkValue[secondPoint] = false;
        }
      },
      chooseChecked() {
        let disableCheck = [0, 2, 7, 10, 14, 15, 19];
        let checkedTable = "";
        let k = 0;
        for (let i = 0; i < this.checkValue.length; i++) {
          if (!(disableCheck.includes(i))) {
            if (this.checkValue[i]) {
              checkedTable += k.toString();
              checkedTable += ',';
            }
            k++;
          }
        }
        // console.log(checkedTable);
        // console.log(checkedTable.slice(0,checkedTable.length-1));
        if(checkedTable!=='')
        this.$emit('get-list', checkedTable.slice(0, checkedTable.length - 1));

        // this.getMatrix(checkedTable.slice(0,checkedTable.length-1));
      }


    },
    beforeMount() {
      this.initArray()
    },
  }
</script>

<style scoped>
  .container {
    margin-top: 90px;
    text-align: center;
    /*margin-right: 100px;*/
    /*margin-left: 100px;*/
    background-color: #D2B48C;
    border-radius: 40px;
  }

  .div-my {
    margin-left: 15px;
    color: darkgreen !important;
  }

  .checkbox {
    text-align: left;
    margin-top: 10px;
    margin-left: 40px;
    padding-top: 10px;
    padding-bottom: 5px;
    font-size: 18px;
    /*color: #492727;*/

  }

  .checkboxes {
    background-color: #FFF8DC;
    border-radius: 30px;
  }


  .heading {
    display: block;
    font-size: 35px;
    font-weight: 700;
    padding: 30px 0;
    border-bottom: 1px solid #ffffff;
    margin-bottom: 30px;
    color: #492727;
  }
  .btn-primary {
    background-color: #FFF8DC;
    border-radius: 20px;
    margin: 20px;
    color: #492727;
    border-color: #D2B48C;
  }
  .btn-primary:hover {
    background-color: #492727;
    color: #D2B48C;
    border-color: #492727;
  }
</style>

