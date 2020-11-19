export const namespaced = false

export const state = {
    token: '',
    user: {
        username: `Александра Пушкина`,
        department: `ВКЦ Ростов`,
        bio: `Я интересуюсь почти всем, но в большинстве своем люблю гонки, мороженое, приключения. Еще обожаю ездить на велосипеде и гулять по набережной`,
        stats: {
            coins: 50000,
            hearts: 100000,
            lightnings: 10000,
        },
        task: {
            taskname: `Название квеста`,
            progress: 84,
            deadline: new Date(2020, 12, 21),
        },
        productivity: 74,
        quality: 93,
        level: 89,
    },
}

export const getters = {
    getUserData: state => state.user,
}
