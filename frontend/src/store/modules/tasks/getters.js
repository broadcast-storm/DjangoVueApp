const getters = {
    allTasksStatus: state => {
        return {
            daily: state.dailyTasksStatus,
            weekly: state.weeklyTasksStatus,
            mainQuest: state.mainQuestStatus,
        }
    },
    dailyTasks: state => {
        return {
            status: state.dailyTasksStatus,
            data: state.dailyTasks,
        }
    },
    weeklyTasks: state => {
        return {
            status: state.weeklyTasksStatus,
            data: state.weeklyTasks,
        }
    },
    mainQuest: state => {
        return {
            status: state.mainQuestStatus,
            data: state.mainQuest,
        }
    },
}

export default getters
