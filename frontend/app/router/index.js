import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from 'pages/MainPage'
import LoginPage from 'pages/LoginPage'
import SignUpPage from 'pages/SignUpPage'

import store from 'store'

Vue.use(VueRouter)

const routes = [
    {
        path: '/login',
        component: LoginPage,
    },
    {
        path: '/signup',
        component: SignUpPage,
    },
    {
        path: '/',
        component: MainPage,
        children: [],
        requiresAuth: true,
    },
    { path: '*', redirect: '/' },
]

let router = new VueRouter({
    routes,
    mode: 'history',
})

router.beforeEach((to, from, next) => {
    const account = store.getters['account/getAccount']
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!account) {
            next({
                path: '/login',
                query: { redirect: to.fullPath },
            })
        } else {
            next({ path: '/' })
        }
    } else {
        next()
    }
})

export default router
