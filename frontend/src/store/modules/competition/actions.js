import axios from 'axios'
import {
    COMPETITION_REQUEST_FETCHING,
    COMPETITION_REQUEST_SUCCESS,
    COMPETITION_REQUEST_ERROR,
} from '@/store/action-types/competition'

const actions = {
    [COMPETITION_REQUEST_FETCHING]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(COMPETITION_REQUEST_FETCHING)
            const response = await axios.get(`/api/competition`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log(response.data)
            commit(COMPETITION_REQUEST_SUCCESS, {
                newProfileInfo: response.data,
            })
        } catch (error) {
            commit(COMPETITION_REQUEST_ERROR, error)
            throw error
        }
    }
}

export default actions