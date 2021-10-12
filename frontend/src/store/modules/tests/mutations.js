import {
    TESTS_REQUEST,
    TESTS_REQUEST_SUCCESS,
    TESTS_REQUEST_ERROR,
    QUESTIONS_REQUEST,
    QUESTIONS_REQUEST_SUCCESS,
    QUESTIONS_REQUEST_ERROR,
    SEND_ANSWERS_REQUEST,
    SEND_ANSWERS_REQUEST_SUCCESS,
    SEND_ANSWERS_REQUEST_ERROR,
} from '@/store/action-types/tests'

const mutations = {
    deleteTest(state, id) {
        state.tests.map(test =>
            test.id === id ? (test.status = 'passed') : test
        )
    },
    [TESTS_REQUEST]: state => {
        state.testsStatus = 'loading'
    },
    [TESTS_REQUEST_SUCCESS]: (state, { newTests }) => {
        state.testsStatus = 'success'
        state.testsList = [...newTests]
    },
    [TESTS_REQUEST_ERROR]: state => {
        state.testsStatus = 'error'
    },
    [QUESTIONS_REQUEST]: state => {
        state.questionsStatus = 'loading'
    },
    [QUESTIONS_REQUEST_SUCCESS]: (state, { newQuestions }) => {
        state.questionsStatus = 'success'
        state.questionsList = { ...newQuestions }
    },
    [QUESTIONS_REQUEST_ERROR]: state => {
        state.questionsStatus = 'error'
    },

    [SEND_ANSWERS_REQUEST]: state => {
        state.sendAnswerStatus = 'sending'
    },
    [SEND_ANSWERS_REQUEST_SUCCESS]: (state, { response }) => {
        state.sendAnswerStatus = 'success'
        state.sendAnswerResult = { ...response }
    },
    [SEND_ANSWERS_REQUEST_ERROR]: state => {
        state.sendAnswerStatus = 'error'
    },
}

export default mutations
