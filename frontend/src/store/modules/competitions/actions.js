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
            const response = await axios.get(
                `http://ygamification.std-1550.ist.mospolytech.ru/api/competition`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `JWT ${token}`,
                    },
                }
            )
            commit(COMPETITIONS_REQUEST_SUCCESS, {
                newCompetitions: response.data,
            })
        } catch (error) {
            commit(COMPETITIONS_REQUEST_ERROR, error)
            throw error
        }
    },
}

export default actions
