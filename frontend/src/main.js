import Vue from 'vue'
import App from './App.vue'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowAltCircleDown } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faArrowAltCircleDown)
Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false 
Vue.use(Buefy)
new Vue({
  render: h => h(App),
}).$mount('#app')
