import { AXIOS_YG_API } from '@/axiosConfig'
import {
    AUTH_REQUEST,
    AUTH_REFRESH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_REFRESH_SUCCESS,
    AUTH_LOGOUT,
    AUTH_REFRESH_ERROR,
    FIRST_AUTH_REQUEST_SUCCESS,
} from '@/store/action-types/tokens'
import { getCookie, deleteCookie } from '@/utils/cookies'

const actions = {
    [AUTH_REQUEST]: async ({ commit }, userCredentials) => {
        try {
            commit(AUTH_REQUEST)
            const response = await AXIOS_YG_API.post('/api/login', {
                headers: {
                    'Content-Type': 'application/json',
                },
                username: userCredentials.username,
                password: userCredentials.password,
            })
            commit(AUTH_SUCCESS, {
                accessToken: response.data.access_token,
                csrfToken: getCookie('csrftoken'),
            })
            commit(FIRST_AUTH_REQUEST_SUCCESS)
            AXIOS_YG_API.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${response.data.access_token}`
            AXIOS_YG_API.defaults.headers['X-CSRFToken'] = getCookie(
                'csrftoken'
            )
        } catch (error) {
            commit(AUTH_ERROR, error)
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
            throw error
        }
    },
    [AUTH_REFRESH_REQUEST]: async ({ commit, state }) => {
        try {
            commit(AUTH_REFRESH_REQUEST)
            const response = await AXIOS_YG_API.post('/api/refresh-token')
            commit(AUTH_REFRESH_SUCCESS, {
                accessToken: response.data.access_token,
            })

            if (!state.firstRequestSuccess) commit(FIRST_AUTH_REQUEST_SUCCESS)

            AXIOS_YG_API.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${response.data.access_token}`
        } catch (error) {
            commit(AUTH_REFRESH_ERROR)
            deleteCookie('csrftoken')
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
            throw error
        }
    },
    [AUTH_LOGOUT]: async ({ commit }) => {
        try {
            const response = await AXIOS_YG_API.post('/api/logout')
            deleteCookie('csrftoken')
            console.log(response)
            commit(AUTH_LOGOUT)
            delete AXIOS_YG_API.defaults.headers.common['Authorization']
        } catch (error) {
            commit(AUTH_ERROR)
            throw error
        }
    },
}

export default actions
