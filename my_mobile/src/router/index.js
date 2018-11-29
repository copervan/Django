import Vue from 'vue'
import Router from 'vue-router'
import IndexPage from '@/components/index'
import Login from '@/components/page/LoginPage'
import diaryView from '@/components/page/Diary/diaryView.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/home'
    },
    {
      path: '/',
      name: 'index',
      component: IndexPage,
      children: [
        {
          path: '/home',
          name: 'home',
          component: resolve => require(['@/components/page/Home'], resolve),
          props: { active: 0 }
        },
        {
          path: '/diary',
          name: 'diary',
          component: resolve => require(['@/components/page/Diary'], resolve),
          props: { active: 1 }
        },
        {
          path: '/notice',
          name: 'notice',
          component: resolve => require(['@/components/page/Notice'], resolve),
          props: { active: 2 }
        },
        {
          path: '/profile',
          name: 'profile',
          component: resolve => require(['@/components/page/Profile'], resolve),
          props: { active: 3 }
        },
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/diaryView/:diary_id',
      name: 'diaryView',
      component: diaryView,
    },
    {
      path: '/poetrys',
      name: 'poetry',
      component: resolve => require(['@/components/page/Poetry/index.vue'], resolve),
    },
    {
      path: '/book/',
      name: 'book',
      component: resolve => require(['@/components/page/Books/index.vue'], resolve),
      children: [
        {
          path: 'chapter/:chapter_id',
          name: 'chapterdetail',
          component: resolve => require(['@/components/page/Books/chapterDetail'], resolve),
          meta: {
            keepAlive: false
          }
        },
        {
          path: '/booklist',
          name: 'booklist',
          component: resolve => require(['@/components/page/Books/bookList.vue'], resolve),
          meta: {
            keepAlive: true
          }
        }
      ]

    },

  ]
})
