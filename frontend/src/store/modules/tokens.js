import { AXIOS_YG_API } from '@/axiosConfig'
import {
    AUTH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_LOGOUT,
} from '@/store/actions/tokens'

export const namespaced = false

export const state = {
    accessToken: localStorage.getItem('accessToken') || null,
    refreshToken: localStorage.getItem('refreshToken') || null,
    status: '',
}

export const getters = {
    isAuthenticated: state => state.accessToken != null,
    authStatus: state => state.status,
}

export const mutations = {
    [AUTH_REQUEST]: state => {
        state.status = 'loading'
    },
    [AUTH_SUCCESS]: (state, { accessToken, refreshToken }) => {
        state.status = 'success'
        state.accessToken = accessToken
        state.refreshToken = refreshToken
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
            return error
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
