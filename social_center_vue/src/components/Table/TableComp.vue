<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-6 d-flex flex-wrap hiden-cont" id="hidediv">
          <div class="hidden-list"  v-for="coll in hiddenCols" v-on:click="returnHideLable($event,coll)">{{coll.label}}</div>


        </div>
        <div style="margin-top: 10px" class="col-4">
          <button v-on:click="clearFilter" type="button" class="btn btn-primary">Очистить фильтры</button>
        </div>
      </div>
    </div>
    <div class="container">
      <table class="table table-bordered table-sm small" style="width:100%">
        <thead>
        <tr>
          <th v-for="l in markingArray" scope="col" v-bind:colspan="l.lenLabels" >
            {{l.nameRUS}}
          </th>
        </tr>
        <tr>
          <th v-for="label in matrixAll.labels" scope="col" class="head-div" v-bind:title="label"
              @contextmenu="getTableIndex($event)+$easycm($event,$root)">
<!--            <div style="z-index: 1; background-color: black; position: absolute;">{{label}}</div>-->
            <div class="myhead">{{label}}</div>
          </th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="line in matrixAll.lines">
          <th class="myth" v-for="col in line" scope="row"><div class="mycol">{{col}}</div></th>
        </tr>

        </tbody>
      </table>
      <easy-cm :list="contextList" :underline="true" :arrow="true" :itemWidth="200" @ecmcb="underConMenu"></easy-cm>

    </div>
  </div>
</template>

<script>

  export default {

    name: "TableComp",
    props: ['matrixAll','notFilterLines','markingArray'],
    data() {
      return {
        lines: [],
        labels: [],
        lastPoint: {
          x: Number,
          y: Number
        },
        hiddenCols:[],
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
        ]
      }
    },
    methods: {
      getTableIndex(event) {
        // console.log(event.target.parentNode)
        // this.lastPoint.y = event.target.parentNode.rowIndex;
        this.lastPoint.y = event.target.parentNode.parentNode.rowIndex-1;
        this.lastPoint.x = event.target.parentNode.cellIndex;
        // this.lastPoint.x = event.target.cellIndex;
        console.log("x:"+this.lastPoint.x+" y:"+this.lastPoint.y);
        this.contextList[0].children = this.getAllChoice();


      },
      getAllChoice() {
        let setBuf = new Set();
        let choices = []
        for (let line in this.matrixAll.lines) {
          setBuf.add(this.matrixAll.lines[line][this.lastPoint.x]);
        }
        setBuf.delete("");
        setBuf.delete(null);
        for (let item of setBuf) {
          choices.push({
            text: item,
            icon: 'iconfont icon-bofang',
            children: []
          })
        }
        return choices;
      },
      moveEmptyLine() {
        let bufArrayGood=[];
        let bufArrayBed=[];
        for (let i in this.matrixAll.lines) {
          if (this.matrixAll.lines[i][this.lastPoint.x] != null && this.matrixAll.lines[i][this.lastPoint.x] !== "") {
            bufArrayGood.push(this.matrixAll.lines[i]);
          }else {
            bufArrayBed.push(this.matrixAll.lines[i]);
          }
        }
        this.matrixAll.lines=bufArrayGood.concat(bufArrayBed);
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
        // console.log(index);
        switch (index[0]) {
          case 0:
            let newLines = [];
            for (let line of this.matrixAll.lines) {
              if (line[this.lastPoint.x] === this.contextList[0].children[index[1]].text) {
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
              x:this.lastPoint.x,
              y:this.lastPoint.y+1,
              label:this.matrixAll.labels[this.lastPoint.x]
            });
            console.log(this.lastPoint.x);
            console.log(this.lastPoint.y);
            let table=document.querySelector('table');
            let count=0;
            for(let make in this.markingArray){
              if(this.lastPoint.x>=this.markingArray[make]['firstPoint'] &&
                this.lastPoint.x<=this.markingArray[make]['lastPoint']){
                console.log(this.markingArray[make]['nameRUS']);
                this.markingArray[make]['lenLabels']--;
                if(this.markingArray[make]['lenLabels']===0){
                  console.log('ноль БЛЯТЬ');
                  table.rows[0].cells[count].style.visibility='hidden';
                  table.rows[0].cells[count].style.display='none';
                }
              }
              count++;
            }
            // console.log(table.rows[this.lastPoint.y].cells[this.lastPoint.x].text);
            table.rows[this.lastPoint.y+1].cells[this.lastPoint.x].style.visibility='hidden';
            table.rows[this.lastPoint.y+1].cells[this.lastPoint.x].style.display='none';
            for(let i=2; i<=this.matrixAll.lines.length+1;i++){
              // console.log(table.rows[this.lastPoint.y+i].cells[this.lastPoint.x]);
              table.rows[this.lastPoint.y+i].cells[this.lastPoint.x].style.visibility='hidden';
              table.rows[this.lastPoint.y+i].cells[this.lastPoint.x].style.display='none';
            }
            // console.log(this.hiddenCols);
            break;
        }


      },
      returnHideLable(event,hideColl){
        event.target.parentNode.removeChild(event.target);
        let table=document.querySelector('table');


        let count=0;
        for(let make in this.markingArray){
          if(hideColl.x>=this.markingArray[make]['firstPoint'] &&
            hideColl.x<=this.markingArray[make]['lastPoint']){
            console.log(this.markingArray[make]['nameRUS']);
            this.markingArray[make]['lenLabels']++;
            if(this.markingArray[make]['lenLabels']!=0){
              table.rows[0].cells[count].style.visibility='visible';
              table.rows[0].cells[count].style.display='table-cell';
            }
          }
          count++;
        }


        table.rows[hideColl.y].cells[hideColl.x].style.visibility='visible';
        table.rows[hideColl.y].cells[hideColl.x].style.display='table-cell';
        for(let i=1; i<=this.matrixAll.lines.length;i++){
          table.rows[hideColl.y+i].cells[hideColl.x].style.visibility='visible';
          table.rows[hideColl.y+i].cells[hideColl.x].style.display='table-cell';
        }
      },
      clearFilter(){
        // console.log("clearFilter");
        // console.log(this.notFilterLines);

        this.matrixAll.lines=this.notFilterLines;
        // this.markingArray=this.notFilterMarking;
        // let mainDiv=document.getElementById('hidediv');
        // let childs=mainDiv.childNodes;
        //
        // console.log(mainDiv);
        // while (childs.length>0){
        //   for(var i=0; i<childs.length; i++){
        //     mainDiv.removeChild(childs[i]);
        //   }
        // }

        let table=document.querySelector('table');
        for(let col of this.hiddenCols){
          table.rows[col.y].cells[col.x].style.visibility='visible';
          table.rows[col.y].cells[col.x].style.display='table-cell';
          for(let i=1; i<=this.matrixAll.lines.length;i++){
            table.rows[col.y+i].cells[col.x].style.visibility='visible';
            table.rows[col.y+i].cells[col.x].style.display='table-cell';
          }
        }
        let count =0;
        for (let make in this.markingArray){
          table.rows[0].cells[count].style.visibility='visible';
          table.rows[0].cells[count].style.display='table-cell';
          this.markingArray[make]['lenLabels']=this.markingArray[make]['lastPoint']-this.markingArray[make]['firstPoint']+1;
          // console.log(this.notFilterMarking[make]['lenLabels']);
          // console.log(this.notFilterMarking[make]);
          // this.markingArray[make]['lenLabels']=this.notFilterMarking[make]['lenLabels'];
          count++;
        }
        console.log(this.markingArray);
        this.hiddenCols=[];
        // table.rows[hideColl.y].cells[hideColl.x].style.visibility='visible';
        // table.rows[hideColl.y].cells[hideColl.x].style.display='table-cell';
        // for(let i=1; i<=this.matrixAll.lines.length;i++){
        //   table.rows[hideColl.y+i].cells[hideColl.x].style.visibility='visible';
        //   table.rows[hideColl.y+i].cells[hideColl.x].style.display='table-cell';
        // }
        // mainDiv.removeChild(mainDiv.childNodes);
        // for (let div of mainDiv.childNodes){
        //   // div.removeChild(div);
        //   console.log(div);
        // }
        // console.log(document.getElementById('hidediv').childNodes);
      }

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
  table{
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
    min-width: 150px;
    max-width: 500px;
    max-height: 200px;



  }
  .myhead{
    /*background-color: red;*/
    /*display:inline-block;*/
    margin: 2px;
    height: 60px;
    overflow: hidden;
    /*white-space: nowrap;*/
    /*white-space: pre-wrap;*/
    text-overflow: ellipsis;
  }
  .mycol{
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
  .hiden-cont{
    border: 2px solid #D2B48C;
    border-radius: 5px;
    margin-left: 20px;
    margin-bottom: 10px;
    margin-right: 10px;
    margin-top: 10px;
    max-height: 100px;
    overflow: auto;
  }
  .hidden-list{
    background-color: #D2B48C;
    border: 2px solid grey;
    margin: 2px;
    border-radius: 5px;
  }
  .hidden-list:hover{
    border-color: red;
  }

</style>
