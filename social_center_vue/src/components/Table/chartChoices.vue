<template>
  <div class="chart-choice">

    <div v-for="butForm in butsForm">
      <p class="h5 title-choice mt-1 ml-1">{{butForm.title}}</p>
      <div class="d-flex bd-highlight pr-1 pl-1">
        <div
          v-for="test in butForm.tests"
          v-bind:hidden="check(test.nameBack)"
          class="p-2 flex-fill bd-highlight btn-choice"
          :class="{'btn-choice-click':test.pressed}"
          @click="pressBut(test)"

        >{{test.nameFront}}
        </div>
      </div>
    </div>


    <div class="d-flex justify-content-between mt-1 ml-1 mr-1 mb-1">
      <div @click="$emit('simple-choice',butsForm) + $emit('show-menu',false)" class="p-2 bd-highlight btn-choice">Построить</div>
<!--      <div @click="$emit('chart-choice',butsForm) + $emit('show-menu',false)" class="p-2 bd-highlight btn-choice">Построить выбранные</div>-->
    </div>

  </div>
</template>

<script>
  export default {
    name: "chartChoices",
    props:['testsList'],
    data: () => ({
      // disable:true,
      titles: ['Первичная диагностика', 'Вторичная диагностика', 'Первичная и Вторичная диагностика'],
      namesFront:['Бойко', 'GAGE', 'SOCRATES'],
      namesBack:[
        ['boykoFirst','GAGEFirst','SOCRATESFirst'],
        ['boykoSecond','GAGESecond','SOCRATESSecond'],
        ['boykoAll','GAGEAll','SOCRATESAll']
      ],
      butsForm: []
    }),
    methods: {
      check(name){

        let i=0;
        for(let n of this.testsList){
          if  (n.includes(name.slice(0,4))){
            i++;
          }
        }
        // console.log("test");
        // console.log(this.testsList);

        if(i===2){
          return false;
        }
        if(this.testsList.includes(name)){
          return false;
        }
        return true;
      },
      pressBut(test) {
        test.pressed = !test.pressed;
      }
    },
    beforeMount() {
      // console.log(this.testsList);
      console.log("gfgdfd");
      for (let i = 0; i < 3; i++) {
        this.butsForm.push({
          title: this.titles[i],
          tests: []
        });
        for (let j = 0; j < 3; j++) {
          this.butsForm[this.butsForm.length-1].tests.push({
            nameFront: this.namesFront[j],
            nameBack: this.namesBack[i][j],
            pressed: false

          });
        }

      }
    }

  }
</script>

<style scoped>
  .chart-choice {
    position: fixed;
    z-index: 999;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    background-color: #FFF8DC;
    width: 50%;
    border: 5px solid #000033;
    border-radius: 10px;
  }

  @media (max-width: 900px) {
    .chart-choice {
      width: 65%;
    }
  }
  @media (max-width: 650px) {
    .chart-choice {
      width: 80%;
    }
  }
  @media (max-width: 420px) {
    .chart-choice {
      width: 98%;
    }
  }


  .title-choice {
    color: #000033;
  }

  .btn-choice {
    background-color: #D2B48C;
    border-radius: 2px;
    /*margin: 5px;*/
    margin: 2px 5px 2px 5px;
    text-align: center;
    /*border: 5px solid #000033;*/
  }

  .btn-choice:hover {
    background-color: #492727;
    color: whitesmoke;

  }

  .btn-choice-click {
    background-color: #D2B48C;
    margin: 2px 5px 2px 5px;
    text-align: center;
    box-shadow: inset 0 10px 10px rgba(0, 10, 20, .5),
    0 1px rgb(83, 94, 104),
    0 0 1px rgb(86, 96, 106);
    border-radius: 4px;
  }

  .btn-choice-click:hover {
    box-shadow: inset 0 10px 10px rgba(0, 10, 20, .2),
    0 1px rgb(83, 94, 104),
    0 0 1px rgb(86, 96, 106);
  }
</style>
