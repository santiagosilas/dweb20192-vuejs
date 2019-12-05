// importing Vue again
import Vue from "vue";

// App is the root component for the application
import App from "./App.vue";

// router setup in router folder
import router from "./router";
import VueRouter from "vue-router";

Vue.use(VueRouter);

// Tells Vue whether or not to show tips and
// warnings in the developer console
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router: router /*inject the router configuration */
}).$mount("#app");
