// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios';
import ElementUI from 'element-ui';
// 默认主题
// import '../static/css/theme-green/index.css';       // 浅绿色主题

import "babel-polyfill";
import Vuex from 'vuex';
// import Iview from 'iview';
// import 'iview/dist/styles/iview.css';

import 'element-ui/lib/theme-chalk/index.css';
import '../static/css/icon.css';

Vue.use(Vuex)
// Vue.use(Iview);
Vue.use(ElementUI, { size: 'small' });
Vue.prototype.$axios = axios;

//使用钩子函数对路由进行权限跳转
router.beforeEach((to, from, next) => {
    const role = localStorage.getItem('ms_username');
    const token = sessionStorage.getItem('token') || ''
    if ( (!role  || !token || typeof token === "undefined")  && to.path !== '/login' ) {
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

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');


// new Vue({
//   el: '#app',
//   router,
//   components: { App },
//   template: '<App/>'
// })
