import { createRouter, createWebHistory } from 'vue-router'
import Login from './components/forms/LoginForm.vue'
import Register from './components/forms/RegisterForm.vue'

const routes = [
  // { path: '/', component: Home },
  { path: '/Login', component: Login },
  { path: '/Register', component: Register },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
