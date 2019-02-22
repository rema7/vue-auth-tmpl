import { ACCOUNT_ERROR, ACCOUNT_REQUEST, ACCOUNT_SUCCESS } from '../actions/Account'
import { getSecured } from 'helpers/requests'

const state = {
    loading: false,
    loaded: false,
    account: null,
}

const getters = {
    getAccount: (state) => state.account,
    isAdmin: (state) => state.account && state.account.admin,
}

const actions = {
    [ACCOUNT_REQUEST]: async ({ state, commit, rootState }) => {
        if (state.loading) {
            return
        }

        commit(ACCOUNT_REQUEST)
        try {
            const result = await getSecured(rootState.settings.urls.account)
            commit(ACCOUNT_SUCCESS, result)
        } catch (e) {
            commit(ACCOUNT_ERROR)
        }
    },
}

const mutations = {
    [ACCOUNT_REQUEST]: (state) => {
        state.loading = true
        state.loaded = false
        state.account = null
    },
    [ACCOUNT_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.account = data
        state.loaded = true
    },
    [ACCOUNT_ERROR]: (state) => {
        state.loading = false
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
