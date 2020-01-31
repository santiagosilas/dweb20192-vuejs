// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

// https://www.npmjs.com/package/vue-toastification
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
Vue.use(Toast, {});

import * as services from "./services/";
Vue.prototype.$services = services;

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    components: { App },
    template: '<App/>'
})