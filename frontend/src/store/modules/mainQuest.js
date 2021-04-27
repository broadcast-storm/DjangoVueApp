export const namespaced = false

export const state = {
    mainQuest: {
        taskname: 'Название квеста',
        progress: 75,
        deadline: '20.04.20',
        subtasks: [
            {
                id: 1,
                taskname: 'Название задачи',
                progress: 75,
                type: 'Еженедельная',
                deadline: '20.04.20',
                reward: {
                    coins: 1000,
                    lightnings: 100,
                },
                difficulty: 'omgveryhard',
                subtasks: [
                    {
                        id: 1,
                        title: 'подзадача',
                        status: 'todo',
                    },
                    {
                        id: 2,
                        title: 'подзадача',
                        status: 'done',
                    },
                    {
                        id: 3,
                        title: 'подзадача',
                        status: 'todo',
                    },
                ],
                desc: 'Описание еженедельной задачи тут да описание',
                status: 'todo',
            },
            {
                id: 2,
                taskname: 'Название задачи',
                progress: 75,
                type: 'Еженедельная',
                deadline: '20.04.20',
                reward: {
                    coins: 1000,
                    lightnings: 100,
                },
                difficulty: 'omgveryhard',
                subtasks: [
                    {
                        id: 1,
                        title: 'подзадача',
                        status: 'todo',
                    },
                    {
                        id: 2,
                        title: 'подзадача',
                        status: 'done',
                    },
                    {
                        id: 3,
                        title: 'подзадача',
                        status: 'todo',
                    },
                ],
                desc: 'Описание еженедельной задачи тут да описание',
                status: 'todo',
            },
            {
                id: 3,
                taskname: 'Название задачи',
                progress: 55,
                type: 'Еженедельная',
                deadline: '20.04.20',
                reward: {
                    coins: 1000,
                    lightnings: 100,
                },
                difficulty: 'omgveryhard',
                subtasks: [
                    {
                        id: 1,
                        title: 'подзадача',
                        status: 'todo',
                    },
                    {
                        id: 2,
                        title: 'подзадача',
                        status: 'done',
                    },
                    {
                        id: 3,
                        title: 'подзадача',
                        status: 'todo',
                    },
                ],
                desc: 'Описание еженедельной задачи тут да описание',
                status: 'todo',
            },
        ],
    },
}

export const getters = {
    getMainQuest: state => state.mainQuest,
    getsubtasks: state => state.subtasks,
}
