import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);
export const store = new Vuex.Store({
  state: {
    baseUrl: 'http://185.209.29.77/',
    // baseUrl: 'http://127.0.0.1:8000/',
  },
  getters: {},
  mutations: {},
  actions: {}
})
