import {
    COMPETITION_REQUEST,
    COMPETITION_REQUEST_SUCCESS,
    COMPETITION_REQUEST_ERROR,
} from '@/store/action-types/competition'

const mutations = {
    [COMPETITION_REQUEST]: state => {
        state.competitionStatus = 'loading'
    },
    [COMPETITION_REQUEST_SUCCESS]: (state, { newCompetition }) => {
        state.competitionStatus = 'success'
        state.competitionList = [...newCompetition]
    },
    [COMPETITION_REQUEST_ERROR]: state => {
        state.competitionStatus = 'error'
    }
}

export default mutations