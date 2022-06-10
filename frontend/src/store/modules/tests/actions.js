import axios from 'axios'
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

const actions = {
    [TESTS_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(TESTS_REQUEST)
            const response = await axios.get(`/api/unresolved_test`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `JWT ${token}`,
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
            const response = await axios.get(
                `/api/test-questions?test_id=${id}`,
                {
                    headers: {
                        'Content-Type': 'application/json',
                        Authorization: `JWT ${token}`,
                    },
                }
            )

            if (response.data === null)
                return commit(QUESTIONS_REQUEST_ERROR, 'not found')

            let questions = []
            response.data.testBlocks.forEach(testBlock => {
                testBlock.questions.forEach(question => {
                    const answerOptions = response.data.answerOptions.filter(
                        answer => answer.question === question.id
                    )
                    const answerIdForNoOption = response.data.answerIds.filter(
                        answer => answer.question === question.id
                    )
                    questions.push({
                        question,
                        answerOptions,
                        answerIdForNoOption,
                    })
                })
            })
            if (questions.length === 0) {
                commit(QUESTIONS_REQUEST_ERROR, 'not found')
            } else
                commit(QUESTIONS_REQUEST_SUCCESS, {
                    newQuestions: {
                        testInfo: response.data.testInfo,
                        questions,
                    },
                })
        } catch (error) {
            commit(QUESTIONS_REQUEST_ERROR, error)
            throw error
        }
    },

    [SEND_ANSWERS_REQUEST]: async (
        { commit, rootState },
        { answers, testId }
    ) => {
        try {
            const token = rootState.tokens.accessToken
            commit(SEND_ANSWERS_REQUEST)
            const data = {
                test_id: testId,
                answers_simple: [],
                answers_multi: [],
                answers_text: [],
            }
            answers.forEach(item => {
                switch (item.answerType) {
                    case 'one_choice':
                        data.answers_simple.push(item.answer)
                        break
                    case 'multi_choice':
                        data.answers_multi.push({
                            question_id: item.question,
                            answer_id: item.answer,
                        })
                        break
                    case 'enter_text':
                    case 'enter_number':
                        data.answers_text.push({
                            question_id: item.question,
                            answer_text: item.answer,
                        })
                        break
                    default:
                        break
                }
            })
            const response = await axios.post(`/api/test-post`, data, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `JWT ${token}`,
                },
            })
            console.log(response.data)
            commit(SEND_ANSWERS_REQUEST_SUCCESS, { response: response.data })
        } catch (error) {
            commit(SEND_ANSWERS_REQUEST_ERROR, error)
            throw error
        }
    },
}

export default actions
