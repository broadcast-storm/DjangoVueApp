import {
    PROFILE_REQUEST_FETCHING,
    PROFILE_REQUEST_SUCCESS,
    PROFILE_REQUEST_ERROR,
} from '@/store/action-types/profile'

const mutations = {
    [PROFILE_REQUEST_FETCHING]: state => {
        state.profileStatus = 'loading'
    },
    [PROFILE_REQUEST_SUCCESS]: (state, { newProfileInfo }) => {
        state.profileStatus = 'success'
        state.profileInfo = { ...newProfileInfo }
    },
    [PROFILE_REQUEST_ERROR]: state => {
        state.profileStatus = 'error'
    },
}

export default mutations
