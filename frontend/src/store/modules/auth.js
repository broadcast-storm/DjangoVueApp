export const namespaced = false

export const state = {
    token: '',
    user: {
        name: 'Александра',
        surname: 'Пушкина',
        patronymic: 'Владимировна',
        photo: require('@/mocks/UserPhoto.jpg'),
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
        achievements: [
            {
                id: '1',
                title: 'Ачивка 1',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/f2c94c',
            },
            {
                id: '2',
                title: 'Ачивка 2',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/6fcf97',
            },
            {
                id: '3',
                title: 'Ачивка 3',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/bb6bd9',
            },
            {
                id: '4',
                title: 'Ачивка 4',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/56ccf2',
            },
            {
                id: '5',
                title: 'Ачивка 5',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/bdbdbd',
            },
            {
                id: '6',
                title: 'Ачивка 6',
                description: 'Какое-то описание',
                status: 'completed',
                img: 'https://via.placeholder.com/150/26bcc2',
            },
            {
                id: '7',
                title: 'Ачивка 7',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
            {
                id: '8',
                title: 'Ачивка 8',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
            {
                id: '9',
                title: 'Ачивка 9',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
            {
                id: '10',
                title: 'Ачивка 10',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
            {
                id: '11',
                title: 'Ачивка 11',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
            {
                id: '12',
                title: 'Ачивка 12',
                description: 'Какое-то описание',
                status: null,
                img: '',
            },
        ],
    },
}

export const getters = {
    getUserData: state => state.user,
}
