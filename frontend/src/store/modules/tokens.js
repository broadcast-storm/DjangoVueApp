import { AXIOS_YG_API } from '@/axiosConfig'
import {
    AUTH_REQUEST,
    AUTH_REFRESH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_REFRESH_SUCCESS,
    AUTH_LOGOUT,
} from '@/store/actions/tokens'

export const namespaced = false

export const state = {
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    status: '',
}

export const getters = {
    isAuthenticated: state =>
        state.accessToken != null && state.refreshToken != null,
    authStatus: state => state.status,
}

export const mutations = {
    [AUTH_REQUEST]: state => {
        state.status = 'loading'
    },
    [AUTH_REFRESH_REQUEST]: state => {
        state.status = 'refreshing'
    },
    [AUTH_SUCCESS]: (state, { accessToken, refreshToken }) => {
        state.status = 'success'
        state.accessToken = accessToken
        state.refreshToken = refreshToken
    },
    [AUTH_REFRESH_SUCCESS]: (state, { accessToken }) => {
        state.status = 'success'
        state.accessToken = accessToken
    },
    [AUTH_ERROR]: state => {
        state.status = 'error'
    },
    [AUTH_LOGOUT]: state => {
        state.status = ''
        state.accessToken = null
        state.refreshToken = null
    },
}

export const actions = {
    [AUTH_REQUEST]: async ({ commit }, userCredentials) => {
        try {
            commit(AUTH_REQUEST)
            const response = await AXIOS_YG_API.post('/api/token/', {
                username: userCredentials.username,
                password: userCredentials.password,
            })
            console.log(response)
            commit(AUTH_SUCCESS, {
                accessToken: response.data.access,
                refreshToken: response.data.refresh,
            })
            AXIOS_YG_API.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${response.data.access}`
            localStorage.setItem('accessToken', response.data.access)
            localStorage.setItem('refreshToken', response.data.refresh)
        } catch (error) {
            commit(AUTH_ERROR, error)
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            throw error
        }
    },
    [AUTH_REFRESH_REQUEST]: async ({ commit, state }) => {
        try {
            commit(AUTH_REFRESH_REQUEST)
            const response = await AXIOS_YG_API.post('/api/token/refresh/', {
                refresh: state.refreshToken,
            })
            console.log(response)
            commit(AUTH_REFRESH_SUCCESS, {
                accessToken: response.data.access,
            })
            AXIOS_YG_API.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${response.data.access}`
            localStorage.setItem('accessToken', response.data.access)
        } catch (error) {
            commit(AUTH_ERROR, error)
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            throw error
        }
    },
    [AUTH_LOGOUT]: ({ commit }) => {
        return new Promise(resolve => {
            commit(AUTH_LOGOUT)
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
            localStorage.removeItem('accessToken')
            localStorage.removeItem('refreshToken')
            resolve()
        })
    },
}
