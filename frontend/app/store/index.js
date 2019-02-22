import Vue from 'vue'
import Vuex from 'vuex'


import account from 'store/modules/Account'
import auth from 'store/modules/Auth'
import settings from 'store/modules/Settings'

Vue.use(Vuex)

const actions = {

}

const state = {
}

const mutations = {
}

const getters = {

}

const modules = {
    account,
    auth,
    settings,
}

export default new Vuex.Store({
    state,
    mutations,
    getters,
    modules,
    actions,
})
