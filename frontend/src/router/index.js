import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import login from '@/components/login'
import dashboard from '@/components/dashboard'
// Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      //	component: HelloWorld
      component: login
    },{
    	path:'/dashboard',
    	component: dashboard, 
    	props: true 
    }
  ]
})