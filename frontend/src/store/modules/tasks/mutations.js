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

const mutations = {
    [WEEKLY_TASKS_REQUEST]: state => {
        state.weeklyTasksStatus = 'loading'
    },
    [WEEKLY_TASKS_SUCCESS]: (state, { newTasks }) => {
        state.weeklyTasksStatus = 'success'
        state.weeklyTasks = [...newTasks]
    },
    [WEEKLY_TASKS_ERROR]: state => {
        state.weeklyTasksStatus = 'error'
    },
    [DAILY_TASKS_REQUEST]: state => {
        state.dailyTasksStatus = 'loading'
    },
    [DAILY_TASKS_SUCCESS]: (state, { newTasks }) => {
        state.dailyTasksStatus = 'success'
        state.dailyTasks = [...newTasks]
    },
    [DAILY_TASKS_ERROR]: state => {
        state.dailyTasksStatus = 'error'
    },
    [MAIN_QUEST_REQUEST]: state => {
        state.mainQuestStatus = 'loading'
    },
    [MAIN_QUEST_SUCCESS]: (state, { newTasks }) => {
        state.mainQuestStatus = 'success'
        state.mainQuest = [...newTasks]
    },
    [MAIN_QUEST_ERROR]: state => {
        state.mainQuestStatus = 'error'
    },
}

export default mutations
