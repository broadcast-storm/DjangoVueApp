import {
    ITEMS_REQUEST,
    ITEMS_SUCCESS,
    ITEMS_ERROR,
} from '@/store/action-types/items'
const mutations = {
    [ITEMS_REQUEST]: state => {
        state.itemsStatus = 'loading'
    },
    [ITEMS_SUCCESS]: (state, { newTasks }) => {
        state.itemsStatus = 'success'
        state.items = [...newTasks]
    },
    [ITEMS_ERROR]: state => {
        state.itemsStatus = 'error'
    },
}
export default mutations
