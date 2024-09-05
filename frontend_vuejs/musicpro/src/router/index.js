import { createRouter, createWebHistory } from 'vue-router'
import CreateView from '../views/CreateView.vue'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ShoppingCartView from '../views/ShoppingCartView.vue'
import SellerView from '../views/SellerView.vue'
import SignUpView from '../views/SignUpView.vue'
import AboutView from '../views/AboutView.vue'
import OrdersView from '../views/OrdersView.vue'
import getUserAdmin from '../functions';

const routes = [
  {
    path: '/create/product',
    name: 'create',
    component: CreateView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/seller/warehouse-stock',
    name: 'seller',
    component: SellerView /*,
    beforeEnter: (to, from, next) => {
    let is_admin = getUserAdmin()
    if (is_admin == null) {
        // user doesn't have access token, redirect to login
        next({ name: 'login' })
    }
    else {
        // user has access token, user can open the page
        next()
    }
  } */
  },
  {
    path: '/shoppingcart',
    name: 'shoppingcart',
    component: ShoppingCartView
  },
  {
    path: '/purchase/orders',
    name: 'orders',
    component: OrdersView
  },
  {
    path: '/about',
    name: 'abour',
    component: AboutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
