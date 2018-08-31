// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview'
import 'iview/dist/styles/iview.css'
import Router from 'vue-router'
import fullcalendar  from 'vue-fullcalendar'
import Vuex from 'vuex'
import VueQuillEditor from 'vue-quill-editor'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'

Vue.use(MintUI)

Vue.use(ElementUI)

Vue.use(Vuex)
Vue.use(fullcalendar)
Vue.config.productionTip = true
Vue.use(iView)
Vue.use(Router)
Vue.use(VueQuillEditor)

const store =  new Vuex.Store({
	state:{
		token: sessionStorage.getItem('token') || ''
	},
	mutations:{
		set_token(state, mytoken) {
			state.token = mytoken
			sessionStorage.setItem('token',mytoken)
			},
		del_token(state) {
			state.token = ''
			}
		}
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
