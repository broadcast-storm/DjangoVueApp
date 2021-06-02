import axios from 'axios'
import {
    PROFILE_REQUEST_FETCHING,
    PROFILE_REQUEST_SUCCESS,
    PROFILE_REQUEST_ERROR,
} from '@/store/action-types/profile'
import jwt from 'jsonwebtoken'

const actions = {
    [PROFILE_REQUEST_FETCHING]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            const userId = jwt.decode(token).user_id
            commit(PROFILE_REQUEST_FETCHING)
            const response = await axios.get(`/api/users/${userId}`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log(response.data)
            commit(PROFILE_REQUEST_SUCCESS, {
                newProfileInfo: response.data,
            })
        } catch (error) {
            commit(PROFILE_REQUEST_ERROR, error)
            throw error
        }
    },
    // [AUTH_REFRESH_REQUEST]: async ({ commit, state }) => {
    //     try {
    //         commit(AUTH_REFRESH_REQUEST)
    //         const response = await axios.post('/api/refresh-token', {
    //             headers: {
    //                 'Content-Type': 'application/json',
    //             },
    //             refresh: state.refreshToken,
    //         })
    //         commit(AUTH_REFRESH_SUCCESS, {
    //             accessToken: response.data.access,
    //         })

    //         if (!state.firstRequestSuccess) commit(FIRST_AUTH_REQUEST_SUCCESS)
    //     } catch (error) {
    //         commit(AUTH_REFRESH_ERROR)
    //         localStorage.removeItem('refresh_token')
    //         throw error
    //     }
    // },
    // [AUTH_LOGOUT]: async ({ commit, state }) => {
    //     try {
    //         await axios.post('/api/logout', {
    //             headers: {
    //                 'Content-Type': 'application/json',
    //             },
    //             refresh_token: state.refreshToken,
    //         })
    //         commit(AUTH_LOGOUT)
    //         localStorage.removeItem('refresh_token')
    //     } catch (error) {
    //         commit(AUTH_ERROR)
    //         throw error
    //     }
    // },
}

export default actions
