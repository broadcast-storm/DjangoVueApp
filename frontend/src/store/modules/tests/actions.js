import axios from 'axios'
import {
    TESTS_REQUEST,
    TESTS_REQUEST_SUCCESS,
    TESTS_REQUEST_ERROR,
    QUESTIONS_REQUEST,
    QUESTIONS_REQUEST_SUCCESS,
    QUESTIONS_REQUEST_ERROR,
} from '@/store/action-types/tests'

const actions = {
    [TESTS_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(TESTS_REQUEST)
            const response = await axios.get(`/api/unresolved_test`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log('tests list:')
            console.log(response.data)
            commit(TESTS_REQUEST_SUCCESS, {
                newTests: response.data,
            })
        } catch (error) {
            commit(TESTS_REQUEST_ERROR, error)
            throw error
        }
    },

    [QUESTIONS_REQUEST]: async ({ commit, rootState }, id) => {
        try {
            const token = rootState.tokens.accessToken
            commit(QUESTIONS_REQUEST)
            const response = await axios.post(`/api/test-questions`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
                test_id: id,
            })
            commit(QUESTIONS_REQUEST_SUCCESS, {
                newQuestions: response.data,
            })
        } catch (error) {
            commit(QUESTIONS_REQUEST_ERROR, error)
            throw error
        }
    },
}

export default actions
