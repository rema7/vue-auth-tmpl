import {
    AUTH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_LOGOUT,
    AUTH_REGISTRATION_REQUEST,
    AUTH_REGISTRATION_SUCCESS,
    AUTH_AUTO_SIGN_IN,
} from 'store/actions/Auth'
import { setToken, removeToken } from 'helpers/storage'
import { post } from 'helpers/requests'

const state = {
    loading: false,
    token: null,
}

const getters = {
    hasToken: (state) => !!state.token,
}

const actions = {
    async [AUTH_REQUEST] ({ state, commit, rootState }, user) {
        if (state.loading) {
            return
        }

        commit(AUTH_REQUEST)
        try {
            const result = await post(
                rootState.settings.urls.login,
                user,
            )
            commit(AUTH_SUCCESS, result)
            return result
        } catch (e) {
            commit(AUTH_ERROR)
        }
    },
    async [AUTH_REGISTRATION_REQUEST] ({ state, commit, rootState }, user) {
        if (state.loading) {
            return
        }

        commit(AUTH_REQUEST)
        try {
            const result = await post(
                rootState.settings.urls.register,
                user,
            )
            commit(AUTH_REGISTRATION_SUCCESS, result)
            return result
        } catch (e) {
            commit(AUTH_ERROR)
        }
    },
    async [AUTH_LOGOUT] ({ state, commit }) {
        commit(AUTH_LOGOUT)
    },
    async [AUTH_AUTO_SIGN_IN] ({ state, commit }, token) {
        commit(AUTH_AUTO_SIGN_IN, token)
    },
}

const mutations = {
    [AUTH_REQUEST]: (state) => {
        state.loading = true
    },
    [AUTH_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.token = data.token
        setToken(data.token)
    },
    [AUTH_REGISTRATION_SUCCESS]: (state, data) => {
        state.loading = false
    },
    [AUTH_ERROR]: (state) => {
        state.loading = false
    },
    [AUTH_LOGOUT]: (state) => {
        state.loading = false
        state.token = null
        removeToken()
    },
    [AUTH_AUTO_SIGN_IN]: (state, token) => {
        state.token = token
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
