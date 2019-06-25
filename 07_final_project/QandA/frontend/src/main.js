import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import sanitizeHTML from 'sanitize-html'

Vue.prototype.$sanitize = sanitizeHTML

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
