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
}

export default actions
