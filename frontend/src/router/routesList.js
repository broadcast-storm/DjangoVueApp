const routesList = {
    mainPage: {
        path: '/',
        header: 'Профиль',
    },
    mainQuestPage: {
        path: '/main-quest',
        header: 'Основной квест',
    },
    competitionsPage: {
        path: '/competitions',
        header: 'Соревнования',
    },
    statisticsPage: {
        path: '/statistics',
        header: 'Статистика',
    },
    shopPage: {
        path: '/shop',
        header: 'Магазин',
        children: {
            shopItems: {
                path: '',
                header: 'Магазин',
            },
            shopItem: {
                path: 'item/:id',
                header: 'Магазин',
            },
            shopCart: {
                path: 'cart',
                header: 'Магазин',
            },
        },
    },
    raitingPage: {
        path: '/raiting',
        header: 'Рейтинг',
    },
    testsPage: {
        path: '/tests',
        header: 'Тесты',
    },
    authPage: {
        path: '/auth',
        header: 'Авторизация',
        children: {
            loginPage: {
                path: '/auth/login',
            },
            forgotpasswordPage: {
                path: '/auth/forgot-password',
            },
        },
    },
}

export default routesList
