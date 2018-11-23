// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import {Form,FormItem,Input as EL_input,Button as EL_Button,Icon as EL_Icon} from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '../static/css/icon.css'
Vue.use(Form).use(FormItem).use(EL_input).use(EL_Button).use(EL_Icon,{ size: 'small' });

import { Tabbar, TabbarItem, Field, Button, Toast } from 'vant';
import { Cell, CellGroup,PullRefresh ,Panel,Icon,List } from 'vant';
import { Swipe, SwipeItem,NavBar,Card ,Dialog} from 'vant';
import { Collapse, CollapseItem,Tag ,Picker} from 'vant';

Vue.use(Collapse).use(CollapseItem).use(Tag).use(Picker).use(Dialog);
Vue.use(Cell).use(CellGroup).use(PullRefresh ).use(NavBar).use(Card);
Vue.use(Swipe).use(SwipeItem).use(Panel).use(Icon).use(List);
Vue.use(Tabbar).use(TabbarItem).use(Field).use(Button).use(Toast);
import 'vant/lib/index.css';

import Vuex from 'vuex';
Vue.use(Vuex)
Vue.config.productionTip = false

import axios from "@/utils/ajaxFunctions";
Vue.prototype.$axios = axios;

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
  const role = localStorage.getItem('ms_username');
  const token = sessionStorage.getItem('token') || ''
  if ((!role || !token || typeof token === "undefined") && to.path !== '/login') {
    next('/login');
  } else if (to.meta.permission) {
    // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
    role === 'admin' ? next() : next('/403');
  } else {
    // 简单的判断IE10及以下不进入富文本编辑器，该组件不兼容
    if (navigator.userAgent.indexOf('MSIE') > -1 && to.path === '/editor') {
      Vue.prototype.$alert('vue-quill-editor组件不兼容IE10及以下浏览器，请使用更高版本的浏览器查看', '浏览器不兼容通知', {
        confirmButtonText: '确定'
      });
    } else {
      next();
    }
  }
})

const store = new Vuex.Store({
  state: {
    token: sessionStorage.getItem('token') || ''
  },
  mutations: {
    set_token(state, mytoken) {
      state.token = mytoken
      sessionStorage.setItem('token', mytoken)
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
