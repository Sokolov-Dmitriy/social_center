import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);
export const store = new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    fullName: '',
    baseUrl: 'https://sokolovds.com/',
    // baseUrl: 'http://127.0.0.1:8000/',
    logIn: 'auth/token/login/',
    clientsList: 'api/clients/',
  },
  getters: {},
  mutations: {
    storeName(state, newName) {
      state.fullName = newName;
    }
  },
  actions: {}
})
