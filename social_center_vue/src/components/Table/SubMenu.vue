<template>
  <div>
    <div style="position: fixed; margin-top: -20px;" class="container-fluid showbtn">
      <div class="d-flex flex-row bd-highlight mb-3 pt-2">
        <div v-bind:hidden="tableShow" class="p-2 bd-highlight item noprint" @click="showTableAll">Таблица</div>
        <div v-bind:hidden="chartsShow" class="p-2 bd-highlight item noprint" @click="showChartsCount">Графики</div>
      </div>
    </div>
    <table-comp v-show="showTable"
                v-bind:matrixAll="matrix"
                v-bind:notFilterLines="notFilterLines"
                v-bind:markingArray="markingArray"
                v-bind:exclusionList="exclusionList"
                v-on:send-data="sendData"
                v-on:open="showChartsCount"
    >
    </table-comp>
    <counting-menu v-if="showCharts===true"
                   v-show="showCharts"
                   v-bind:chartDat="chartsData"
                   v-bind:gotChart="showCharts"
    ></counting-menu>
    <!--                v-bind:marking="marking"-->


    <!--    <p style="visibility: visible">ttttt{{matrix.get('labels')}}</p>-->
  </div>
</template>

<script>
  import TableComp from "./TableComp";
  import CountingMenu from "./CountingMenu";

  export default {
    name: "SubMenu",
    props: ['matrix', 'markingArray'],
    data() {
      return {
        showTable: true,
        notFilterLines: this.matrix.lines,
        exclusionList: {
          fio: ['ФИО клиента'],
          general: [
            '№', 'Код', 'Пришли', 'Зависимость', 'Количество вз', 'Н/л', 'Наличие судимости', 'Состояние зависимости',
            'Трудовая занятость', 'ВИЧ-статус', 'взр', 'Количество детей', 'Неопределен', 'В окне', 'Мал.', 'Дев.', 'Муж.',
            'Жен.', 'Категория', 'Адрес, телефон', 'Паспортные данные', 'Дата постановки', 'Какое сопровождение',
            'Дети (ФИО)', 'М/О', '?'
          ],
          generalInformation: [
            'Дата рождения',
            'Где, кем работает (при наличии работы)',
            'Причина, по которой не работает'
          ],
          alcoholDrugsClient: [
            'Вид наркотика'
          ],
          chronicDisease: [
            'Как часто посещает центр СПИД',
            'Причина, по которой не получает лечение ВИЧ'
          ],
          child: [
            'ФИО',
            'Дата рождения',
            'Какое образовательное учреждение'
          ],
          generalInformationFamily: [],
          husbendInformation: [
            'ФИО мужа/партнёра',
            'Адрес',
            'Телефон',
            'Дата рождения',
            'Где, кем работает (при наличии работы)',
            'Причина, по которой не работает',
            'Вид наркотика'
          ],
          socialLivingConditions: [
            'Жилая площадь в расчете на человека (кв.м.)',
            'Сумма задолженности (в рублях)'

          ],
          socialEconomConditions: [
            'Причина,по которой не оформлены льготы'
          ],
          expertOpinion: [
            'Другие сведения о клиенте и членах семьи, сообщённые во время диагностического интервью',
            'Ожидания клиента от помощи социальной службы (запрос)',
            'Личные впечатления специалиста от взаимодействия с клиентом',
            'Имя специалиста',
            'Фамилия специалиста'
          ],
          boykoFirst: [],
          GAGEFirst: [],
          SOCRATESFirst: [],
          boykoSecond: [],
          GAGESecond: [],
          SOCRATESSecond: []

        },
        chartsData: [],
        showCharts: false,
        tableShow: true,
        chartsShow: false
        // readyFilter:this.markingArray.filterMarking,
        // notFilter:this.markingArray.notFilterMarking
        // matrixAll:{
        //   labels:this.matrix.labels,
        //   lines:this.matrix.lines,
        //   notFilterLines:this.matrix.lines
        // }
      }
    },
    components: {
      TableComp,
      CountingMenu
    },
    methods: {
      sendData(data) {
        console.log("sendData");
        console.log(data);
        this.chartsData = data;
        this.showCharts = true;

      },
      showTableAll() {
        this.tableShow = true;
        this.showTable = true;
        this.chartsShow = false;
        this.showCharts = false;
        console.log("showTable");
      },
      showChartsCount() {
        if (this.chartsData.length === 0) {
          alert("Графики не построены!")
        }
          // console.log(this.chartsData);
        // if(this.showCharts) {
        else {
          this.tableShow = false;
          this.showTable = false;
          this.chartsShow = true;
          // }
          this.showCharts = true;
        }
        console.log("showCharts");
      }
    }
  }
</script>

<style scoped>
  .item {
    background-color: grey;
    /*padding: 5px 10px;*/
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;

  }

  .item:hover {
    opacity: 0.7;
    /*border-radius: 10px;*/
  }

  @media print {
    .item.noprint {
      display: none;
    }
  }

  .showbtn {
    position: fixed;
    /*top: 68px;*/
    top: 80px;
    z-index: 998;
    background-color: #FFF8DC;
    padding-bottom: 5px;
  }
</style>

