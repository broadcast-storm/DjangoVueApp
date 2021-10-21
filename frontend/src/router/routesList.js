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
        children: {
            SearchCompetitions: {
                path: '',
                header: 'Соревнования',
            },
            CurrentCompetitions: {
                path: 'versus',
                header: 'Соревнования',
            },
        },
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
    ratingPage: {
        path: '/rating',
        header: 'Рейтинг',
    },
    testsPage: {
        path: '/tests',
        header: 'Тесты',
        children: {
            testsList: {
                path: '',
                header: 'Список тестов',
            },
            testPage: {
                path: ':id',
                header: 'Тест',
            },
        },
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
