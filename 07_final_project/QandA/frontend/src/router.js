import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Question from './views/Question.vue'
import QuestionEditor from './views/QuestionEditor.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  // let's not append the base url to our paths
  // base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/ask',
      name: 'ask',
      component: QuestionEditor
    },
    {
      path: '/question/:slug',
      name: 'question',
      component: Question,
      props: true
    }
  ]
})
