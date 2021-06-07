import axios from 'axios'
import {
    WEEKLY_TASKS_REQUEST,
    WEEKLY_TASKS_SUCCESS,
    WEEKLY_TASKS_ERROR,
    DAILY_TASKS_REQUEST,
    DAILY_TASKS_SUCCESS,
    DAILY_TASKS_ERROR,
    MAIN_QUEST_REQUEST,
    MAIN_QUEST_SUCCESS,
    MAIN_QUEST_ERROR,
} from '@/store/action-types/tasks'

const actions = {
    [WEEKLY_TASKS_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(WEEKLY_TASKS_REQUEST)
            const response = await axios.get(`/api/get-weekly-tasks`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log('weekly:')
            console.log(response.data)
            commit(WEEKLY_TASKS_SUCCESS, {
                newTasks: response.data,
            })
        } catch (error) {
            commit(WEEKLY_TASKS_ERROR, error)
            throw error
        }
    },

    [DAILY_TASKS_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(DAILY_TASKS_REQUEST)
            const response = await axios.get(`/api/get-daily-tasks`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log('daily:')
            console.log(response.data)
            commit(DAILY_TASKS_SUCCESS, {
                newTasks: response.data,
            })
        } catch (error) {
            commit(DAILY_TASKS_ERROR, error)
            throw error
        }
    },

    [MAIN_QUEST_REQUEST]: async ({ commit, rootState }) => {
        try {
            const token = rootState.tokens.accessToken
            commit(MAIN_QUEST_REQUEST)
            const response = await axios.get(`/api/get-quests`, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`,
                },
            })
            console.log('quests:')
            console.log(response.data)
            commit(MAIN_QUEST_SUCCESS, {
                newTasks: response.data,
            })
        } catch (error) {
            commit(MAIN_QUEST_ERROR, error)
            throw error
        }
    },
}

export default actions
