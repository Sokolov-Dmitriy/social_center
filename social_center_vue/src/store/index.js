import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
export const store = new Vuex.Store({
  state: {
    baseUrl: 'https://v325098.hosted-by-vdsina.ru/',
    // baseUrl: 'http://127.0.0.1:8000/',
  },
  getters: {},
  mutations: {},
  actions: {}
})
