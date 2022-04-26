import {
    COMPETITIONS_REQUEST,
    COMPETITIONS_REQUEST_SUCCESS,
    COMPETITIONS_REQUEST_ERROR,
} from '@/store/action-types/competitions'

const mutations = {
    [COMPETITIONS_REQUEST]: state => {
        state.competitionStatus = 'loading'
    },
    [COMPETITIONS_REQUEST_SUCCESS]: (state, { newCompetitions }) => {
        state.competitionStatus = 'success'
        state.competitions = [...newCompetitions]
    },
    [COMPETITIONS_REQUEST_ERROR]: state => {
        state.competitionStatus = 'error'
    },
}

export default mutations
