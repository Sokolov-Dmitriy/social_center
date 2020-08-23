<template>
  <div class="container-fluid mt-3 ">
    <div class="d-flex flex-column">
      <div class="row">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>Выбрать все</b></div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" id="0" v-model="checkValue[0]"
                   v-on:click="chooseAll(checkValue[0])" v-bind:checked="checkValue[0]">
          </div>
        </div>
      </div>

      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>Сведения о клиенте(общее)</b></div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-bind:checked="checkValue[1]" v-model="checkValue[1]">
          </div>
        </div>
      </div>

      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hideFirstBlock">
            <b>1. Сведения о клиенте</b>
            <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide1===false"></i>
            <i class="fa fa-caret-right" aria-hidden="true" v-if="hide1===true"></i>
          </div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" id="1" v-on:click="setChoose(checkValue[2],3,5)"
                   v-model="checkValue[2]" v-bind:checked="checkValue[2]">
          </div>
        </div>
      </div>
      <div class="div-my" v-bind:hidden="hide1">
        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>1.1. Общая информация</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[3],2)" v-model="checkValue[3]"
                     v-bind:checked="checkValue[3]">
            </div>
          </div>
        </div>

        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>1.2. Информация о противоправных
              действиях,
              правонарушениях, употреблении наркотиков, алкоголя</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[4],2)" v-model="checkValue[4]"
                     v-bind:checked="checkValue[4]">
            </div>
          </div>
        </div>

        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>1.3. Информация о наличии
              хронического
              заболевания</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my align-self-start" type="checkbox" v-on:click="setFalse(checkValue[5],2)"
                     v-model="checkValue[5]" v-bind:checked="checkValue[5]">
            </div>
          </div>
        </div>
      </div>

      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>2. Сведения о детях</b></div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-bind:checked="checkValue[6]" v-model="checkValue[6]">
          </div>
        </div>
      </div>

      <!--      <div class="row mt-1">-->
      <!--        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">-->
      <!--          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hideSecondBlock">-->
      <!--            <b>2. Сведения о детях</b>-->
      <!--            <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide2===false"></i>-->
      <!--            <i class="fa fa-caret-right" aria-hidden="true" v-if="hide2===true"></i>-->
      <!--          </div>-->
      <!--          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">-->
      <!--            <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[6],7,8)" v-model="checkValue[6]"-->
      <!--                   v-bind:checked="checkValue[6]">-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->
      <!--      <div class="div-my" v-bind:hidden="hide2">-->
      <!--        <div class="row mt-1 ml-3">-->
      <!--          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">-->
      <!--            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>2.1. Общая информация</b></div>-->
      <!--            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">-->
      <!--              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[7],6)" v-model="checkValue[7]"-->
      <!--                     v-bind:checked="checkValue[7]">-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </div>-->

      <!--        <div class="row mt-1 ml-3">-->
      <!--          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">-->
      <!--            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>2.2. Информация о состоянии здоровья ребёнка</b></div>-->
      <!--            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">-->
      <!--              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[8],6)" v-model="checkValue[8]"-->
      <!--                     v-bind:checked="checkValue[8]">-->
      <!--            </div>-->
      <!--          </div>-->
      <!--        </div>-->
      <!--      </div>-->


      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hideSecondBlock">
            <b>3. Сведения о членах семьи</b>
            <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide2===false"></i>
            <i class="fa fa-caret-right" aria-hidden="true" v-if="hide2===true"></i>
          </div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[7],8,9)"
                   v-model="checkValue[7]" v-bind:checked="checkValue[7]">
          </div>
        </div>
      </div>
      <div class="div-my" v-bind:hidden="hide2">
        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>3.1. Общие сведения</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[8],7)" v-model="checkValue[8]"
                     v-bind:checked="checkValue[8]">
            </div>
          </div>
        </div>

        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>3.2. Информация о
              муже/партнёре</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[9],7)"
                     v-model="checkValue[9]" v-bind:checked="checkValue[9]">
            </div>
          </div>
        </div>


      </div>


      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hideThirdBlock">
            <b>4. Сведения о социально-бытовом и
              социально-экономическом положении</b>
            <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide3===false"></i>
            <i class="fa fa-caret-right" aria-hidden="true" v-if="hide3===true"></i>
          </div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[10],11,12)"
                   v-model="checkValue[10]" v-bind:checked="checkValue[10]">
          </div>
        </div>
      </div>
      <div class="div-my" v-bind:hidden="hide3">
        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>4.1. Социально-бытовые
              условия </b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[11],10)"
                     v-model="checkValue[11]" v-bind:checked="checkValue[11]">
            </div>
          </div>
        </div>

        <div class="row mt-1 ml-3">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>4.2. Социально-экономические
              условия проживания</b></div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[12],10)"
                     v-model="checkValue[12]" v-bind:checked="checkValue[12]">
            </div>
          </div>
        </div>


      </div>


      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right"><b>5. Заключение специалиста</b></div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-bind:checked="checkValue[13]" v-model="checkValue[13]">
          </div>
        </div>
      </div>

      <!--      занесение тестов -->
      <div class="row mt-1">
        <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
          <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hide4Block">
            <b>6.Тесты</b>
            <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide4===false"></i>
            <i class="fa fa-caret-right" aria-hidden="true" v-if="hide4===true"></i>
          </div>
          <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
            <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[14],15,22)"
                   v-model="checkValue[14]" v-bind:checked="checkValue[14]">
          </div>
        </div>
      </div>

      <div class="div-my" v-bind:hidden="hide4">

        <div class="row mt-1">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hide5Block">
              <b>Первичная диагностика</b>
              <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide5===false"></i>
              <i class="fa fa-caret-right" aria-hidden="true" v-if="hide5===true"></i>
            </div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[15],16,18)"
                     v-model="checkValue[15]" v-bind:checked="checkValue[15]">
            </div>
          </div>
        </div>

        <div class="div-my" v-bind:hidden="hide5">
          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>Бойко</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[16],15)"
                       v-model="checkValue[16]" v-bind:checked="checkValue[16]">
              </div>
            </div>
          </div>

          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>GAGE</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[17],15)"
                       v-model="checkValue[17]" v-bind:checked="checkValue[17]">
              </div>
            </div>
          </div>

          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>SOCRATES</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[18],15)"
                       v-model="checkValue[18]" v-bind:checked="checkValue[18]">
              </div>
            </div>
          </div>


        </div>


        <div class="row mt-1">
          <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
            <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right" @click="hide6Block">
              <b>Вторичная диагностика</b>
              <i class="fa fa-sort-desc fa-2x" aria-hidden="true" v-if="hide6===false"></i>
              <i class="fa fa-caret-right" aria-hidden="true" v-if="hide6===true"></i>
            </div>
            <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
              <input class="checkbox-my" type="checkbox" v-on:click="setChoose(checkValue[19],20,22)"
                     v-model="checkValue[19]" v-bind:checked="checkValue[19]">
            </div>
          </div>
        </div>

        <div class="div-my" v-bind:hidden="hide6">
          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>Бойко</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[20],19)"
                       v-model="checkValue[20]" v-bind:checked="checkValue[20]">
              </div>
            </div>
          </div>

          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>GAGE</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[21],19)"
                       v-model="checkValue[21]" v-bind:checked="checkValue[21]">
              </div>
            </div>
          </div>

          <div class="row mt-1 ml-3">
            <div class="col-xl-5 col-lg-5 col-md-7 col-sm-9 col-12 row">
              <div class="col-xl-11 col-lg-11 col-md-11 col-sm-11 col-10 text-right">
                <b>SOCRATES</b></div>
              <div class="col-xl-1 col-lg-1 col-md-1 col-sm-1 col-2">
                <input class="checkbox-my" type="checkbox" v-on:click="setFalse(checkValue[22],19)"
                       v-model="checkValue[22]" v-bind:checked="checkValue[22]">
              </div>
            </div>
          </div>


        </div>

      </div>


    </div>
    <button type="button" class="btn btn-primary" v-on:click="chooseChecked">Сформировать таблицу</button>
  </div>
</template>

<script>
  import $ from "jquery";

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
  .checkbox-my {
    width: 20px;
    height: 20px;
    position: absolute;
    top: 50%;
    margin-top: -10px;
  }

  .div-my {
    color: seagreen;
  }
</style>

