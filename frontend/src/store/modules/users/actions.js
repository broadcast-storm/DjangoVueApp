import axios from 'axios'
import {
    USERS_REQUEST_FETCHING,
    USERS_REQUEST_SUCCESS,
    USERS_REQUEST_ERROR,
} from '@/store/action-types/users'

const actions = {
    [USERS_REQUEST_FETCHING]: async ({ commit,rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            const response = await axios.get(
                `http://ygamification.std-1550.ist.mospolytech.ru/api/users`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `JWT ${token}`,
                    },
                }
            )
            commit(USERS_REQUEST_SUCCESS, {
                newUsers: response.data,
            })
        } catch (error) {
            commit(USERS_REQUEST_ERROR, error)
            throw error
        }
    },
}

export default actions
