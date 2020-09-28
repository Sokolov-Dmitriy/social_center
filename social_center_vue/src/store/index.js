import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
export const store = new Vuex.Store({
  state: {
    baseUrl: 'https://sokolovds.com/',
    // baseUrl: 'http://127.0.0.1:8001/',
  },
  getters: {},
  mutations: {},
  actions: {}
})
