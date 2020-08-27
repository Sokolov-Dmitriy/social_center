<template>
  <div v-show="showMe">


    <div style="position: fixed; margin-top: -20px;" class="container-fluid big">
      <div class="row">
        <div class="col-md-5 col-sm-4 col-sm-11 d-flex flex-wrap hiden-cont ml-2 mr-2" id="hidediv">
          <div class="hidden-list" v-for="coll in hiddenCols" v-on:click="returnHideLable($event,coll)">{{coll.label}}
          </div>
        </div>
        <div class="col-md-6 col-sm-11 d-flex flex-row bd-highlight mt-sm-1 mb-sm-1 mt-1 mb-1 mt-md-0 mb-md-0 mybutmin">
          <div class="bd-highlight mr-1"><button v-on:click="clearFilter" type="button" class="btn btn-primary" id="oneb">Очистить фильтры</button></div>
          <div class="bd-highlight ml-1"><button v-on:click="buildCharts" type="button" class="btn btn-primary" id="twob">Построить графики</button></div>
        </div>
      </div>
    </div>


    <div class="container smaller">
      <table class="table table-bordered table-sm small" style="width:100%">
        <thead>
        <tr class="title">
          <th v-for="l in markingArray" scope="col" v-bind:colspan="l.lenLabels">
            {{l.nameRUS}}
          </th>
        </tr>
        <tr>
          <th v-for="label in matrixAll.labels"
              style="background-color: rgba(216, 228, 188, 0.5)"
              v-on:click="rightClickOnLabel"
              scope="col"
              class="head-div"
              v-bind:title="label"
          >
            <!--            <div style="z-index: 1; background-color: black; position: absolute;">{{label}}</div>-->
            <div class="myhead" @contextmenu="getTableIndex($event)+$easycm($event,$root)">{{label}}</div>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="line in matrixAll.lines">
          <th class="myth" v-for="col in line" scope="row">
            <div class="mycol">{{col}}</div>
          </th>
        </tr>

        </tbody>
      </table>
      <easy-cm :list="contextList" :underline="true" :arrow="true" :itemWidth="200" @ecmcb="underConMenu"></easy-cm>

    </div>
  </div>
</template>

<script>

  import $ from "jquery";

  export default {

    name: "TableComp",
    props: ['matrixAll', 'notFilterLines', 'markingArray', 'exclusionList'],
    data() {
      return {
        lines: [],
        labels: [],
        lastPoint: {
          x: Number,
          y: Number
        },
        hiddenCols: [],
        contextList: [
          {
            text: 'Фильтр',
            icon: 'iconfont icon-bofang',
            children: []
          },
          {
            text: 'Сотрировать',
            icon: 'iconfont icon-bofang',
            children: [
              {
                text: 'по возрастанию',
                icon: 'iconfont icon-bofang',
                children: []
              },
              {
                text: 'по убыванию',
                icon: 'iconfont icon-bofang',
                children: []
              }
            ]
          },
          {
            text: 'Скрыть',
            icon: 'iconfont icon-bofang',
            children: []
          }
        ],
        selectLabels: {
          simpleField: [],
          childField: [],
          testField: []
        },
        testName: ['boykoFirst',
          'GAGEFirst',
          'SOCRATESFirst',
          'boykoSecond',
          'GAGESecond',
          'SOCRATESSecond'],
        showMe: true,
        testChoices: {
          boyko: [],
          GAGE: [],
          SOCRATES: []
        },
        arTest: [],
        specialSimpleField: [
          'Возраст',
          'Длительность употрбления (в годах)',
          'Длительность ремиссии (в годах)(наркотики)',
          'Длительность ремиссии (в годах)(алкоголь)',
          'Предположительное время инфицирования (в годах)',
        ]
      }
    },
    methods: {
      isChild(index) {
        for (let make in this.markingArray) {
          if (index >= this.markingArray[make]['firstPoint'] &&
            index <= this.markingArray[make]['lastPoint'] && make.includes('child')) {
            return true;
          }
        }
        return false;
      },
      getTableIndex(event) {
        // console.log(this.markingArray);
        // console.log(event.target.parentNode)
        // this.lastPoint.y = event.target.parentNode.rowIndex;
        this.lastPoint.y = event.target.parentNode.parentNode.rowIndex - 1;
        this.lastPoint.x = event.target.parentNode.cellIndex;
        console.log("x:" + this.lastPoint.x + " y:" + this.lastPoint.y);
        console.log(this.selectLabels);
        this.contextList[0].children = this.getAllChoice();
      },
      rightClickOnLabel(event) {
        // this.getTestsChoices();
        let y = event.target.parentNode.parentNode.rowIndex;
        let x = event.target.parentNode.cellIndex;
        console.log(x + ' ' + y);
        console.log(this.matrixAll.labels[x]);
        if (event.target.parentNode.style.backgroundColor != 'rgba(87, 151, 67, 0.5)') {
          for (var make in this.markingArray) {
            if (x >= this.markingArray[make]['firstPoint'] &&
              x <= this.markingArray[make]['lastPoint']) {
              if (!make.includes('child')) {
                if (this.exclusionList[make].indexOf(this.matrixAll.labels[x]) === -1 && this.testName.indexOf(make) === -1) {
                  console.log('можно');
                  this.selectLabels.simpleField.push(x);
                  event.target.parentNode.style.backgroundColor = 'rgba(87, 151, 67, 0.5)';
                  // console.log(event.target.parentNode);
                } else {
                  if (this.testName.indexOf(make) !== -1) {
                    console.log(make);
                    // let firstPoint = this.markingArray[make]['firstPoint'];
                    // let lastPoint = this.markingArray[make]['lastPoint'];
                    for (let i = this.markingArray[make]['firstPoint']; i <= this.markingArray[make]['lastPoint']; i++) {
                      event.target.parentNode.parentNode.childNodes[i].style.backgroundColor = 'rgba(87, 151, 67, 0.5)';
                    }
                    this.selectLabels.testField.push(make.toString());
                  }
                }
              } else {
                if (this.exclusionList['child'].indexOf(this.matrixAll.labels[x]) === -1) {
                  this.selectLabels.childField.push([]);
                  this.selectLabels.childField[this.selectLabels.childField.length - 1].push(x);
                  let labelName = this.matrixAll.labels[x];
                  let step = this.markingArray[make]['lastPoint'] - this.markingArray[make]['firstPoint'] + 1;
                  let point = x - 20;
                  let bufName = this.matrixAll.labels[point];
                  // console.log('step'+step);
                  event.target.parentNode.parentNode.childNodes[x].style.backgroundColor = 'rgba(87, 151, 67, 0.5)';
                  while (labelName === bufName) {
                    this.selectLabels.childField[this.selectLabels.childField.length - 1].push(point);
                    event.target.parentNode.parentNode.childNodes[point].style.backgroundColor = 'rgba(87, 151, 67, 0.5)';
                    point -= step;
                    if (point < 1) break;
                    bufName = this.matrixAll.labels[point];
                    // console.log('точка  '+bufName + ' ' + point + '' + labelName);
                  }
                  point = x + step;
                  bufName = this.matrixAll.labels[point];
                  while (labelName === bufName) {
                    this.selectLabels.childField[this.selectLabels.childField.length - 1].push(point);
                    event.target.parentNode.parentNode.childNodes[point].style.backgroundColor = 'rgba(87, 151, 67, 0.5)';
                    point += step;
                    if (point > this.matrixAll.labels.length) break;
                    bufName = this.matrixAll.labels[point];
                  }
                  this.selectLabels.childField[this.selectLabels.childField.length - 1] = this.selectLabels.childField[this.selectLabels.childField.length - 1].sort();
                  console.log('ребенок');
                }


              }
              // if(this.exclusionList[make].indexOf(this.matrixAll.labels[x])===-1){
              //   console.log('можно');
              //   let buf=make.toString();
              //   if(buf.toString().includes('child')){
              //     console.log('ребенок');
              //   }
            }
            // console.log(this.exclusionList[make]);
          }
        } else {
          for (var make in this.markingArray) {
            if (x >= this.markingArray[make]['firstPoint'] &&
              x <= this.markingArray[make]['lastPoint']) {
              if (!make.includes('child')) {
                if (this.exclusionList[make].indexOf(this.matrixAll.labels[x]) === -1 && this.testName.indexOf(make) === -1) {
                  console.log('можно');
                  // this.selectLabels.simpleField.push(x);
                  this.selectLabels.simpleField = this.selectLabels.simpleField.filter(item => item !== x);
                  // this.selectLabels.simpleField = this.selectLabels.simpleField.slice(this.selectLabels.simpleField.indexOf(x), 1);
                  event.target.parentNode.style.backgroundColor = 'rgba(216, 228, 188, 0.5)';
                  // console.log(event.target.parentNode);
                } else {
                  if (this.testName.indexOf(make) !== -1) {
                    console.log(make);
                    // let firstPoint = this.markingArray[make]['firstPoint'];
                    // let lastPoint = this.markingArray[make]['lastPoint'];
                    for (let i = this.markingArray[make]['firstPoint']; i <= this.markingArray[make]['lastPoint']; i++) {
                      event.target.parentNode.parentNode.childNodes[i].style.backgroundColor = 'rgba(216, 228, 188, 0.5)';
                    }
                    // this.selectLabels.testField.push(make.toString());
                    // console.log('slice ' + this.selectLabels.testField.slice(this.selectLabels.testField.indexOf(make.toString()), 1));
                    // let index=this.selectLabels.testField.indexOf(make.toString());
                    // console.log('index '+index);
                    // this.selectLabels.testField.slice(index, 1)
                    // this.selectLabels.testField = this.selectLabels.testField.filter(function(item) {
                    //   return item !== value
                    // })
                    this.selectLabels.testField = this.selectLabels.testField.filter(item => item !== make.toString());
                    // this.selectLabels.testField=this.selectLabels.testField.slice(this.selectLabels.testField.indexOf(make.toString()),1);
                  }
                }
              } else {
                if (this.exclusionList['child'].indexOf(this.matrixAll.labels[x]) === -1) {
                  // this.selectLabels.childField.push([]);
                  let bufArray = [];
                  // this.selectLabels.childField[this.selectLabels.childField.length - 1].push(x);
                  bufArray.push(x);
                  let labelName = this.matrixAll.labels[x];
                  let step = this.markingArray[make]['lastPoint'] - this.markingArray[make]['firstPoint'] + 1;
                  let point = x - 20;
                  let bufName = this.matrixAll.labels[point];
                  // console.log('step'+step);
                  event.target.parentNode.parentNode.childNodes[x].style.backgroundColor = 'rgba(216, 228, 188, 0.5)';
                  while (labelName === bufName) {
                    // this.selectLabels.childField[this.selectLabels.childField.length - 1].push(point);
                    bufArray.push(point);
                    event.target.parentNode.parentNode.childNodes[point].style.backgroundColor = 'rgba(216, 228, 188, 0.5)';
                    point -= step;
                    if (point < 1) break;
                    bufName = this.matrixAll.labels[point];
                    // console.log('точка  '+bufName + ' ' + point + '' + labelName);
                  }
                  point = x + step;
                  bufName = this.matrixAll.labels[point];
                  while (labelName === bufName) {
                    // this.selectLabels.childField[this.selectLabels.childField.length - 1].push(point);
                    bufArray.push(point);
                    event.target.parentNode.parentNode.childNodes[point].style.backgroundColor = 'rgba(216, 228, 188, 0.5)';
                    point += step;
                    if (point > this.matrixAll.labels.length) break;
                    bufName = this.matrixAll.labels[point];
                  }
                  console.log('ребенок');
                  for (let i in this.selectLabels.childField) {
                    if (this.selectLabels.childField[i].length === bufArray.length && this.selectLabels.childField[i].sort().every(function (value, index) {
                      return value === bufArray.sort()[index]
                    })) {
                      console.log("gooooood");
                      bufArray = [];
                      for (let j in this.selectLabels.childField) {
                        if (j != i) bufArray.push(this.selectLabels.childField[j]);
                      }
                      break;
                    }
                  }
                  this.selectLabels.childField = bufArray;
                }
              }
            }
          }
        }
      },
      getAllChoice() {
        let x = this.lastPoint.x;
        let setBuf = new Set();
        let choices = [];
        if (!this.specialSimpleField.includes(this.matrixAll.labels[x])) {
          for (let line in this.matrixAll.lines) {
            setBuf.add(this.matrixAll.lines[line][x]);
          }
          setBuf.delete("");
          setBuf.delete(null);
          for (let item of setBuf) {
            choices.push({
              text: item,
              min: item,
              max: item,
              icon: 'iconfont icon-bofang',
              children: []
            })
          }
        } else {
          if (this.isChild(x)) {
            if (this.specialSimpleField.indexOf(this.matrixAll.labels[x]) === 0) {
              choices.push({
                text: 'До 3 лет',
                min: 0,
                max: 3,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От 4 до 6',
                min: 4,
                max: 6,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От 7 до 17',
                min: 7,
                max: 17,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От 18 и старше',
                min: 18,
                max: 99999,
                icon: 'iconfont icon-bofang',
                children: []
              });
            }
          } else {
            if (this.specialSimpleField.indexOf(this.matrixAll.labels[x]) === 0) {
              choices.push({
                text: 'До 18',
                min: 0,
                max: 17,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От 18 до 35',
                min: 18,
                max: 35,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От 36 и выше',
                min: 36,
                max: 99999,
                icon: 'iconfont icon-bofang',
                children: []
              });
            } else if ([1, 2, 3, 4].includes(this.specialSimpleField.indexOf(this.matrixAll.labels[x]))) {
              choices.push({
                text: 'До года',
                min: 0,
                max: 0.99,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От года до двух',
                min: 1,
                max: 1.99,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От двух до трех',
                min: 2,
                max: 2.99,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От трех до пяти',
                min: 3,
                max: 4.99,
                icon: 'iconfont icon-bofang',
                children: []
              });
              choices.push({
                text: 'От пяти и выше',
                min: 5,
                max: 99999,
                icon: 'iconfont icon-bofang',
                children: []
              });
            }
          }
        }
        return choices;
      },
      moveEmptyLine() {
        let bufArrayGood = [];
        let bufArrayBed = [];
        for (let i in this.matrixAll.lines) {
          if (this.matrixAll.lines[i][this.lastPoint.x] != null && this.matrixAll.lines[i][this.lastPoint.x] !== "") {
            bufArrayGood.push(this.matrixAll.lines[i]);
          } else {
            bufArrayBed.push(this.matrixAll.lines[i]);
          }
        }
        this.matrixAll.lines = bufArrayGood.concat(bufArrayBed);
      },
      upToDownSort(x) {
        this.matrixAll.lines.sort(function (a, b) {
          let nA = a[x];
          let nB = b[x];
          if (nA < nB)
            return 1;
          if (nA > nB)
            return -1;
          return 0;
        });
        this.moveEmptyLine();
      },
      downToUpSort(x) {
        this.matrixAll.lines.sort(function (a, b) {
          let nA = a[x];
          let nB = b[x];
          if (nA < nB)
            return -1;
          if (nA > nB)
            return 1;
          return 0;
        });
        this.moveEmptyLine();
      },
      underConMenu(index) {
        console.log('index' + index);
        switch (index[0]) {
          case 0:
            let newLines = [];
            let bufArray = [];
            for (let line of this.matrixAll.lines) {
              if (line[this.lastPoint.x] !== "" && line[this.lastPoint.x] != null) {
                bufArray.push(line);
              }
            }
            for (let line of bufArray) {
              if (line[this.lastPoint.x] >= this.contextList[0].children[index[1]].min &&
                line[this.lastPoint.x] <= this.contextList[0].children[index[1]].max) {
                newLines.push(line);
              }
            }
            this.matrixAll.lines = newLines;
            break;
          case 1:
            let x = this.lastPoint.x;
            switch (index[1]) {
              case 0:
                this.downToUpSort(x);
                break;
              case 1:
                this.upToDownSort(x);
                break;
            }
            break;
          case 2:
            console.log("скрыть");
            this.hiddenCols.push({
              x: this.lastPoint.x,
              y: this.lastPoint.y + 1,
              label: this.matrixAll.labels[this.lastPoint.x]
            });
            console.log(this.lastPoint.x);
            console.log(this.lastPoint.y);
            let table = document.querySelector('table');
            let count = 0;
            for (let make in this.markingArray) {
              if (this.lastPoint.x >= this.markingArray[make]['firstPoint'] &&
                this.lastPoint.x <= this.markingArray[make]['lastPoint']) {
                console.log(this.markingArray[make]['nameRUS']);
                this.markingArray[make]['lenLabels']--;
                if (this.markingArray[make]['lenLabels'] === 0) {
                  console.log('ноль БЛЯТЬ');
                  table.rows[0].cells[count].style.visibility = 'hidden';
                  table.rows[0].cells[count].style.display = 'none';
                }
              }
              count++;
            }
            // console.log(table.rows[this.lastPoint.y].cells[this.lastPoint.x].text);
            table.rows[this.lastPoint.y + 1].cells[this.lastPoint.x].style.visibility = 'hidden';
            table.rows[this.lastPoint.y + 1].cells[this.lastPoint.x].style.display = 'none';
            for (let i = 2; i <= this.matrixAll.lines.length + 1; i++) {
              // console.log(table.rows[this.lastPoint.y+i].cells[this.lastPoint.x]);
              table.rows[this.lastPoint.y + i].cells[this.lastPoint.x].style.visibility = 'hidden';
              table.rows[this.lastPoint.y + i].cells[this.lastPoint.x].style.display = 'none';
            }
            // console.log(this.hiddenCols);
            break;
        }


      },
      returnHideLable(event, hideColl) {
        event.target.parentNode.removeChild(event.target);
        let table = document.querySelector('table');


        let count = 0;
        for (let make in this.markingArray) {
          if (hideColl.x >= this.markingArray[make]['firstPoint'] &&
            hideColl.x <= this.markingArray[make]['lastPoint']) {
            console.log(this.markingArray[make]['nameRUS']);
            this.markingArray[make]['lenLabels']++;
            if (this.markingArray[make]['lenLabels'] != 0) {
              table.rows[0].cells[count].style.visibility = 'visible';
              table.rows[0].cells[count].style.display = 'table-cell';
            }
          }
          count++;
        }


        table.rows[hideColl.y].cells[hideColl.x].style.visibility = 'visible';
        table.rows[hideColl.y].cells[hideColl.x].style.display = 'table-cell';
        for (let i = 1; i <= this.matrixAll.lines.length; i++) {
          table.rows[hideColl.y + i].cells[hideColl.x].style.visibility = 'visible';
          table.rows[hideColl.y + i].cells[hideColl.x].style.display = 'table-cell';
        }
      },
      clearFilter() {
        let len = this.matrixAll.lines.length;
        this.matrixAll.lines = this.notFilterLines;
        let table = document.querySelector('table');
        for (let col of this.hiddenCols) {
          table.rows[col.y].cells[col.x].style.visibility = 'visible';
          table.rows[col.y].cells[col.x].style.display = 'table-cell';
          for (let i = 0; i < len; i++) {
            console.log(table.rows[i + 2].cells[col.x]);
            table.rows[i + 2].cells[col.x].style.visibility = 'visible';
            table.rows[i + 2].cells[col.x].style.display = 'table-cell';
          }
        }
        let count = 0;
        for (let make in this.markingArray) {
          table.rows[0].cells[count].style.visibility = 'visible';
          table.rows[0].cells[count].style.display = 'table-cell';
          this.markingArray[make]['lenLabels'] = this.markingArray[make]['lastPoint'] - this.markingArray[make]['firstPoint'] + 1;
          count++;
        }
        console.log(this.markingArray);
        this.hiddenCols = [];
      },
      /**
       * проверка, пустой ли подпункт(для детей, т.к. данных может не быть, но строки присусттвуют):
       * @param x
       * @param y
       * @returns {boolean}
       */
      isEpmty(x, y) {
        console.log('isSimple');
        for (var make in this.markingArray) {
          if (x >= this.markingArray[make]['firstPoint'] &&
            x <= this.markingArray[make]['lastPoint'] &&
            make.includes('child')) {
            for (let i = this.markingArray[make]['firstPoint']; i <= this.markingArray[make]['lastPoint']; i++) {
              if (this.matrixAll.lines[y][i] !== "" && this.matrixAll.lines[y][i] != null) {
                return false;
              }
            }
            return true;
          }
        }
      },
      /**
       * возвращает все значения в столбце, кол-во их вхождений и кол-во полей всего
       * @param arrayNum - индексы полей
       * @returns {{names: [], counts: [], count: number}}
       */
      countFieldForChart(arrayNum) {
        let setBuf = new Set();
        let countEmptyLine = 0;
        let forChart = {
          counts: [],
          names: [],
          count: 0,
        };
        for (let index of arrayNum) {
          for (let line of this.matrixAll.lines) {
            setBuf.add(line[index]);
          }
        }
        for (let index of arrayNum) {
          for (let lineI in this.matrixAll.lines) {
            if (this.matrixAll.lines[lineI][index] === "" || this.matrixAll.lines[lineI][index] == null) {
              if (!this.isEpmty(index, lineI)) {
                countEmptyLine++;
              }
            }
          }
        }
        setBuf.delete("");
        setBuf.delete(null);
        for (let item of setBuf) {
          let counter = 0;
          for (let index of arrayNum) {
            for (let line of this.matrixAll.lines) {
              if (line[index] === item) {
                counter++;
              }
            }
          }
          forChart.counts.push(counter);
          forChart.names.push(item);

        }
        forChart.counts.push(countEmptyLine);
        forChart.names.push('Не указано');
        for (let count of forChart.counts) {
          forChart.count += count;
        }

        return forChart;
      },
      simpleCharts(nameI, label) {
        let chart = {
          chartData: {
            labels: [],
            labelMe: this.matrixAll.labels[label],
            heightMy: 50,
            // labels: [this.matrixAll.labels[point]],
            datasets: []
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
                  let label = context.dataset.label;
                  let max = context.chart.scales['x-axis-0'].end;
                  // let strr = '<div>'+
                  //   label.toString()+
                  //   '</br>'+
                  //   Math.round(value / max * 100).toString()+
                  //   '% / '+
                  //   value.toString()+
                  //   '</div>';
                  // return label + '\n ' + Math.round(value / max * 100) + '% / ' + value;
                  return Math.round(value / max * 100) + '% / ' + value;
                  // return strr;
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 0,
                    stepSize: 0
                  },
                },
              ],
            },
          }
        }
        let buf = this.countFieldForChart(nameI);
        for (let i = 0; i < buf.names.length; i++) {
          chart.chartData.datasets.push({
            label: buf.names[i],
            backgroundColor: '#' + (Math.random().toString(16) + '000000').substring(2, 8).toUpperCase(),
            data: [buf.counts[i]]
          });
        }
        chart.chartData.heightMy += chart.chartData.datasets.length * 50;
        chart.options.scales.xAxes[0].ticks.max = buf.count;
        chart.options.scales.xAxes[0].ticks.stepSize = buf.count / 10;
        return chart;
      },
      specialFieldWithYears(nameI, label, groups) {
        let chart = {
          chartData: {
            labels: [],
            labelMe: this.matrixAll.labels[label],
            heightMy: 50,
            datasets: []
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
                  let label = context.dataset.label;
                  let max = context.chart.scales['x-axis-0'].end;
                  return Math.round(value / max * 100) + '% / ' + value;
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 0,
                    stepSize: 0
                  },
                },
              ],
            },
          }
        }
        let buf = this.countFieldForChart(nameI);
        for (let i = 0; i < buf.names.length; i++) {
          for (let group of groups) {
            if (buf.names[i] >= group.min && buf.names[i] <= group.max) {
              group.count += buf.counts[i];
              break;
            }
          }
        }
        for (let group of groups) {
          if (group.count > 0) {
            chart.chartData.datasets.push({
              label: group.name,
              backgroundColor: '#' + (Math.random().toString(16) + '000000').substring(2, 8).toUpperCase(),
              data: [group.count]
            });
          }
        }
        if (buf.names.indexOf('Не указано') !== -1) {
          chart.chartData.datasets.push({
            label: buf.names[buf.names.indexOf('Не указано')],
            backgroundColor: '#' + (Math.random().toString(16) + '000000').substring(2, 8).toUpperCase(),
            data: [buf.counts[buf.names.indexOf('Не указано')]]
          });
        }
        chart.chartData.heightMy += chart.chartData.datasets.length * 50;
        chart.options.scales.xAxes[0].ticks.max = buf.count;
        chart.options.scales.xAxes[0].ticks.stepSize = buf.count / 10;
        return chart;
      },
      getTestsChoices() {
        let ar;
        // let res = new Map();
        $.ajax({
          url: this.$store.state.baseUrl + "api/" + "tests" + "/",
          type: "GET",
          success: (response) => {
            this.arTest = response.data;
            for (let num in response.data['boyko']) {
              // console.log(num);
              this.testChoices.boyko.push({
                labelName: response.data['boyko'][num]['label'],
                answers: response.data['boyko'][num]['answers']
              });
            }
          },
          error: (response) => {
            if (response.status === 401) this.logOut();
          }
        })

        return ar;
        // return res;
      },
      testGAGESolve(typeTest) {
        let kinds = [
          'Результаты первичной диагностики по методике GAGE',
          'Результаты вторичной диагностики по методике GAGE'
        ];
        let test = {
          inter: [],
          fullBalls: []
        };
        test.inter = {
          chartData: {
            labels: ['Риск зависимости', 'Риск злоупотребления'],
            heightMy: 150,
            labelMe: kinds[typeTest],
            // labels: [this.matrixAll.labels[point]],
            datasets: [
              {
                label: 'Среднее значение по каждому из пунктов',
                backgroundColor: 'red',
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
                  return value.toFixed(2);
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 28,
                    stepSize: 28 / 10
                  },
                },
              ],
            },
          }
        };
        let GAGEType = [
          'GAGEFirst',
          'GAGESecond'
        ];
        let lastPoint;
        let allSumCount = {
          sum1: 0,
          sum2: 0,
          allSum: 0,
          counter: 0,
        };
        for (let value in this.markingArray) {
          if (value === GAGEType[typeTest]) {
            lastPoint = this.markingArray[value]['lastPoint'];
            break;
          }
        }
        for (let line of this.matrixAll.lines) {
          if (line[lastPoint - 2] !== "" && line[lastPoint - 2] != null) {
            allSumCount.sum1 += parseInt(line[lastPoint - 2], 10);
            allSumCount.sum2 += parseInt(line[lastPoint - 4], 10);
            allSumCount.counter++;
          }
        }
        allSumCount.allSum = allSumCount.sum1 + allSumCount.sum2;
        test.inter.chartData.datasets[0].data.push(allSumCount.sum1 / allSumCount.counter);
        test.inter.chartData.datasets[0].data.push(allSumCount.sum2 / allSumCount.counter);
        return test;
      },
      testSOCRATESSolve(typeTest) {
        let kinds = [
          'Результаты первичной диагностики по методике SOCRATES',
          'Результаты вторичной диагностики по методике SOCRATES'
        ];
        let test = {
          inter: [],
          fullBalls: []
        };
        test.inter = {
          chartData: {
            labels: ['Действие', 'Амбивалентность', 'Осознание'],
            labelMe: kinds[typeTest],
            heightMy: 200,
            // labels: [this.matrixAll.labels[point]],
            datasets: [
              {
                label: 'Среднее значение по каждому из пунктов',
                backgroundColor: 'red',
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
                  return value.toFixed(2);
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 40,
                    stepSize: 40 / 10
                  },
                },
              ],
            },
          }
        };
        let SOCRATESType = [
          'SOCRATESFirst',
          'SOCRATESSecond'
        ];
        let lastPoint;
        let allSumCount = {
          sum1: 0,
          sum2: 0,
          sum3: 0,
          allSum: 0,
          counter: 0,
        };
        for (let value in this.markingArray) {
          if (value === SOCRATESType[typeTest]) {
            lastPoint = this.markingArray[value]['lastPoint'];
            break;
          }
        }
        for (let line of this.matrixAll.lines) {
          if (line[lastPoint - 2] !== "" && line[lastPoint - 2] != null) {
            allSumCount.sum1 += parseInt(line[lastPoint - 8], 10);
            allSumCount.sum2 += parseInt(line[lastPoint - 6], 10);
            allSumCount.sum3 += parseInt(line[lastPoint - 4], 10);
            allSumCount.allSum += parseInt(line[lastPoint - 2], 10);
            allSumCount.counter++;
          }
        }
        test.inter.chartData.datasets[0].data.push(allSumCount.sum3 / allSumCount.counter);
        test.inter.chartData.datasets[0].data.push(allSumCount.sum2 / allSumCount.counter);
        test.inter.chartData.datasets[0].data.push(allSumCount.sum1 / allSumCount.counter);
        test.fullBalls = {
          chartData: {
            labels: [],
            labelMe: 'Общая оценка готовности к изменениям',
            // labels: [this.matrixAll.labels[point]],
            datasets: [
              {
                label: 'Средняя сумма значений',
                backgroundColor: 'blue',
                data: [allSumCount.allSum / allSumCount.counter]
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
                  return value.toFixed(2);
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 95,
                    stepSize: 95 / 10
                  },
                },
              ],
            },
          }
        };
        // console.log(allSumCount.sum1);
        // console.log(allSumCount.sum2);
        // console.log(allSumCount.sum3);
        // console.log(allSumCount.allSum);
        // console.log(allSumCount.counter);


        return test;
      },
      testBoykoSolve(typeTest) {
        let kinds = [
          'Результаты первичной диагностики по методике Бойко Е.О.',
          'Результаты вторичной диагностики по методике Бойко Е.О.'
        ];
        let test = {
          inter: [],
          fullBalls: []
        };
        test.inter = {
          chartData: {
            labels: [],
            labelMe: kinds[typeTest],
            heightMy: 550,
            // labels: [this.matrixAll.labels[point]],
            datasets: [
              {
                label: 'Среднее значение по каждому из пунктов',
                backgroundColor: 'red',
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
                  return value.toFixed(2);
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 4,
                    stepSize: 4 / 10
                  },
                },
              ],
            },
          }
        };
        let boykoType = [
          'boykoFirst',
          'boykoSecond'
        ];
        let firstPoint;
        let lastPoint;
        let sumBalls = 0;
        let counter = 0;
        let allSumCount = [0, 0];
        for (let value in this.markingArray) {
          if (value === boykoType[typeTest]) {
            firstPoint = this.markingArray[value]['firstPoint'];
            lastPoint = this.markingArray[value]['lastPoint'];
            break;
          }
        }
        for (let i = firstPoint; i <= firstPoint + 9; i++) {
          let label = this.matrixAll.labels[i];
          test.inter.chartData.labels.push(label);
          for (let line of this.matrixAll.lines) {
            let answer = line[i];
            for (var value of this.testChoices.boyko) {
              if (value.labelName === label) {
                for (let answerIterator = 0; answerIterator < value.answers.length; answerIterator++) {
                  if (answer === value.answers[answerIterator]) {
                    counter++;
                    sumBalls += answerIterator;
                    break;
                  }
                }
                break;
              }
            }
          }
          test.inter.chartData.datasets[0].data.push(sumBalls / counter);
          allSumCount[0] += sumBalls;
          allSumCount[1] = counter;
          // console.log('cont:' + counter + " sum:" + sumBalls);
          counter = 0;
          sumBalls = 0;
        }
        test.fullBalls = {
          chartData: {
            labels: [],
            labelMe: 'Общая оценка социального функционирования',
            // labels: [this.matrixAll.labels[point]],
            datasets: [
              {
                label: 'Средняя сумма значений',
                backgroundColor: 'blue',
                data: [allSumCount[0] / allSumCount[1]]
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
                  return value.toFixed(2);
                }
              }
            },
            scales: {
              xAxes: [
                {
                  ticks: {
                    min: 0,
                    max: 40,
                    stepSize: 4 / 10
                  },
                },
              ],
            },
          }
        };
        // console.log('avg:'+allSumCount[0]/allSumCount[1]);
        // console.log(allSumCount[0]+'avg:'+allSumCount[1]);

        return test;

      },
      buildCharts() {
        let forBuldCharts = {
          simple: [],
          tests: [],
          childs: []
        };
        for (let label of this.selectLabels.testField) {
          let switchElement;
          for (let i = 0; i < this.testName.length; i++) {
            if (label === this.testName[i]) {
              switchElement = i;
              break;
            }
          }
          switch (switchElement) {
            case 0:
              forBuldCharts.tests.push(this.testBoykoSolve(0));
              break;
            case 1:
              forBuldCharts.tests.push(this.testGAGESolve(0));
              break;
            case 2:
              forBuldCharts.tests.push(this.testSOCRATESSolve(0));
              break;
            case 3:
              forBuldCharts.tests.push(this.testBoykoSolve(1));
              break;
            case 4:
              forBuldCharts.tests.push(this.testGAGESolve(1));
              break;
            case 5:
              forBuldCharts.tests.push(this.testSOCRATESSolve(1));
              break;
          }
        }
        for (let label of this.selectLabels.simpleField) {
          if (!this.specialSimpleField.includes(this.matrixAll.labels[label])) {
            forBuldCharts.simple.push(this.simpleCharts([label], label));
          } else {
            if (this.specialSimpleField.indexOf(this.matrixAll.labels[label]) === 0) {
              forBuldCharts.simple.push(this.specialFieldWithYears([label], label, [
                {
                  name: 'До 18',
                  min: 0,
                  max: 17,
                  count: 0
                },
                {
                  name: 'От 18 до 35',
                  min: 18,
                  max: 35,
                  count: 0
                },
                {
                  name: 'От 36 и выше',
                  min: 36,
                  max: 99999,
                  count: 0
                }
              ]));
            } else if ([1, 2, 3, 4].includes(this.specialSimpleField.indexOf(this.matrixAll.labels[label]))) {
              forBuldCharts.simple.push(this.specialFieldWithYears([label], label, [
                {
                  name: 'До года',
                  min: 0,
                  max: 0.99,
                  count: 0
                },
                {
                  name: 'От года до двух',
                  min: 1,
                  max: 1.99,
                  count: 0
                },
                {
                  name: 'От двух до трех',
                  min: 2,
                  max: 2.99,
                  count: 0
                },
                {
                  name: 'От трех до пяти',
                  min: 3,
                  max: 4.99,
                  count: 0
                },
                {
                  name: 'От пяти и выше',
                  min: 5,
                  max: 99999,
                  count: 0
                }
              ]));
            }
          }
        }
        for (let arrayLabel of this.selectLabels.childField) {
          if (!this.specialSimpleField.includes(this.matrixAll.labels[arrayLabel[0]])) {
            forBuldCharts.childs.push(this.simpleCharts(arrayLabel, arrayLabel[0]));
          } else {
            if (this.specialSimpleField.indexOf(this.matrixAll.labels[arrayLabel[0]]) === 0) {
              forBuldCharts.childs.push(this.specialFieldWithYears(arrayLabel, arrayLabel[0], [
                {
                  name: 'До 3 лет',
                  min: 0,
                  max: 3,
                  count: 0
                },
                {
                  name: 'От 4 до 6',
                  min: 4,
                  max: 6,
                  count: 0
                },
                {
                  name: 'От 7 до 17',
                  min: 7,
                  max: 17,
                  count: 0
                },
                {
                  name: 'От 18 и старше',
                  min: 18,
                  max: 99999,
                  count: 0
                },
              ]));
            }
          }
        }


        if (forBuldCharts.simple.length !== 0 ||
          forBuldCharts.tests.length !== 0 ||
          forBuldCharts.childs.length !== 0) {
          this.showMe = false;
          this.$emit('send-data', forBuldCharts);
          this.$emit('open');
        } else {
          alert('Поля не выбраны!');
        }
      }

    },
    beforeMount() {
      this.getTestsChoices();
    }
  }
</script>

<style scoped>
  .container {
    margin: 0;
    padding: 0;
  }

  .myth {
    min-width: 100px;
    max-width: 500px;
    max-height: 200px;
  }

  /*thead{*/
  /*  max-height: 200px!important;*/
  /*}*/
  table {
    /*table-layout: fixed;*/
    /*width: 100%;*/
  }

  .head-div {
    /*position: relative;*/
    /*max-width: 150px;*/
    /*min-width: 100px;*/
    /*min-height: 30px;*/
    /*max-height: 150px;*/
    /*overflow: hidden;*/
    /*text-overflow: ellipsis;*/
    /*width: 100%;*/
    /*text-align: left;*/
    padding: 0;
    margin: 0;
    min-width: 150px;
    max-width: 500px;
    max-height: 200px;


  }

  .myhead {
    /*background-color: red;*/
    /*display:inline-block;*/
    /*margin: 2px;*/
    height: 60px;
    overflow: hidden;
    /*white-space: nowrap;*/
    /*white-space: pre-wrap;*/
    text-overflow: ellipsis;
    padding: 2px;
  }

  .mycol {
    max-height: 100px;
    overflow: auto;
    white-space: pre-wrap;
  }

  .head-div .close-icon {

    position: absolute;
    visibility: hidden;
    top: 10px;
    right: 10px;
    width: 2em;
    height: 2em;
  }

  .close-icon:hover {
    border: 1px;
    border-color: red;
    stroke: red;
  }

  .head-div .sort-icon {
    position: absolute;
    margin-right: auto;
    margin-left: auto;
    padding-right: 15px;
    bottom: 0px;
    width: 100%;
    height: 30px;
    fill: black;

  }

  .sort-icon:hover {
    fill: green;
  }

  /*th {*/
  /*  border: 2px;*/
  /*  border-color: grey;*/
  /*}*/
  th:hover {

    border-bottom-color: red;
  }

  .head-div:hover .close-icon {
    visibility: visible;
  }

  .hiden-cont {
    border: 2px solid #D2B48C;
    border-radius: 5px;
    /*margin-left: 20px;*/
    /*margin-bottom: 10px;*/
    /*margin-right: 10px;*/
    /*margin-top: 10px;*/
    /*height: 60px;*/
    /*max-height: 60px;*/
    min-height: 30px;
    overflow: auto;
  }

  .hidden-list {
    background-color: #D2B48C;
    border: 2px solid grey;
    margin: 2px;
    border-radius: 5px;
    height: 28px;
  }

  .hidden-list:hover {
    border-color: red;
  }

  .btn-primary {
    background-color: #D2B48C;
    color: #492727;
    border-color: #D2B48C;
    /*height: 38px;*/
    /*margin-bottom: 10px;*/
    /*margin-top: 10px;*/
  }

  .btn-primary:hover {
    background-color: #492727;
    color: #D2B48C;
  }

  .big {
    position: fixed;
    padding-top: 10px;
    /*padding-bottom: 10;*/
    /*top: 68px;*/
    top: 126px;
    z-index: 998;
    background-color: #FFF8DC;
    width: 100%;
  }

  .smaller {
    z-index: 1;
    margin-top: 200px;
  }

  .title {
    background-color: #D2B48C;
    background-color: rgba(210, 180, 140, 0.5);
  }
  @media(max-width: 396px){
    .smaller{
      margin-top: 150px!important;
    }
    .btn-primary{
      /*height: 48px;*/
      /*font-size: 14px;*/
      /*text-transform: lowercase;*/
      /*vertical-align: text-top!important;*/
    }
    .hiden-cont{
      visibility: hidden;
      display: none;

    }
    #twob{
      margin-left: 7px!important;
      /*margin-right: auto!important;*/
      /*margin-left: auto!important;*/
      /*display: none;*/
    }
    #oneb{
      /*right: 0!important;*/
      display: none;

    }
    .mybutmin{
      /*align-content: right!important;*/
    }
    .big{
      margin: 0;
      z-index: 997;
      padding: 0;
      top:94px;

    }

  }

</style>
