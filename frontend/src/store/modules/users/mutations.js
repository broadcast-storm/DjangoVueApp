import {
    USERS_REQUEST,
    USERS_REQUEST_SUCCESS,
    USERS_REQUEST_ERROR,
} from '@/store/action-types/users'

const mutations = {
    [USERS_REQUEST]: state => {
        state.usersStatus = 'loading'
    },
    [USERS_REQUEST_SUCCESS]: (state, { newUsers }) => {
        state.usersStatus = 'success'
        state.users = [...newUsers]
    },
    [USERS_REQUEST_ERROR]: state => {
        state.usersStatus = 'error'
    },
}

export default mutations
