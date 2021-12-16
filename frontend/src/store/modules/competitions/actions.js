import axios from 'axios'
import {
    COMPETITIONS_REQUEST_FETCHING,
    COMPETITIONS_REQUEST_SUCCESS,
    COMPETITIONS_REQUEST_ERROR,
} from '@/store/action-types/competitions'

const actions = {
    [COMPETITIONS_REQUEST_FETCHING]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(COMPETITIONS_REQUEST_FETCHING)
            const response = await axios.get(`/api/competition`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log(response.data)
            commit(COMPETITIONS_REQUEST_SUCCESS, {
                newProfileInfo: response.data,
            })
        } catch (error) {
            commit(COMPETITIONS_REQUEST_ERROR, error)
            throw error
        }
    }
}

export default actions