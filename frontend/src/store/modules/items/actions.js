import axios from 'axios'
import {
    ITEMS_REQUEST,
    ITEMS_SUCCESS,
    ITEMS_ERROR,
} from '@/store/action-types/items'

const actions = {
    [ITEMS_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(ITEMS_REQUEST)
            const response = await axios.get(`/api/shop`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `JWT ${token}`,
                },
            })
            console.log('items:')
            console.log(response.data)
            commit(ITEMS_SUCCESS, {
                newItems: response.data,
            })
        } catch (error) {
            commit(ITEMS_ERROR, error)
            throw error
        }
    },
}
export default actions
