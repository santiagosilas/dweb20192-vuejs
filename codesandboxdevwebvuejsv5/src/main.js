/*eslint-disable */
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueRouter from "vue-router";

import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

import * as http from './resources/';

Vue.use(VueRouter);

// Objeto para comunicacao entre os componentes irmaos
Vue.prototype.$eventHub = new Vue();

Vue.prototype.$http = http;

Vue.config.productionTip = false;

new Vue({
    render: h => h(App),
    router: router
}).$mount("#app");