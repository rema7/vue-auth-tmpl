import Vue from 'vue'
import VeeValidate from 'vee-validate'
import axios from 'axios'


import store from './store/index'
import router from './router'
import i18n from './i18n'

import App from './App.vue'

import { removeToken } from 'helpers/storage'
import { AUTH_LOGOUT } from 'store/actions/Auth'
import { SETTINGS_REQUEST } from 'store/actions/Settings'
import { ACCOUNT_REQUEST } from 'store/actions/Account'

import './index.scss'


axios.interceptors.response.use((response) => {
    return response
}, (error) => {
    if (error.response && error.response.status === 401) {
        removeToken()
        store.dispatch('auth/' + AUTH_LOGOUT)
        const fullPath = window.location.pathname
        if (fullPath !== '/login' && fullPath !== 'signup') {
            router.push({
                path: '/login',
                query: {
                    redirect: fullPath !== '/login' ? fullPath : null,
                },
            })
        }
    }
    throw error
})

axios.defaults.validateStatus = (status) => {
    return status === 200
}

Vue.use(VeeValidate, {
    inject: false,
})

store.dispatch('settings/' + SETTINGS_REQUEST).then(() => {
    store.dispatch('account/' + ACCOUNT_REQUEST).then(() => {
        /* eslint-disable-next-line no-new */
        new Vue({
            el: '#app',
            i18n,
            store,
            router,
            render: (h) => h(App),
        })
    })
})

