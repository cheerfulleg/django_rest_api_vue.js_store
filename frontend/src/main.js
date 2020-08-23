import Vue from 'vue'
import App from './App.vue'
import './assets/styles/styles.scss'
import store from "@/store/store";
import router from "@/router/router";
import "material-design-icons-iconfont"
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
