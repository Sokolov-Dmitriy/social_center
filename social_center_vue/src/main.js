// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import {router} from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import BootstrapVue, {BootstrapVueIcons} from "bootstrap-vue"
import "bootstrap-vue/dist/bootstrap-vue.css"
import "font-awesome/css/font-awesome.min.css"
import VueEasyCm from 'vue-easycm'
import {store} from "./store";
import LogOutFunc from "./logoutFunction"

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueEasyCm)
Vue.use(LogOutFunc)

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
