import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import LoginForm from '@/views/AuthViews/LoginForm'
import ForgotPassword from '@/views/AuthViews/ForgotPassword'
import routesList from '@/router/routesList'
import store from '../store'

Vue.use(VueRouter)

const routes = [
    {
        path: routesList.mainPage.path,
        component: Main,
        children: [
            {
                path: routesList.mainPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Profile.vue'),
                },
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.competitionsPage.path,
                components: {
                    'main-router': () =>
                        import(
                            '@/views/MainViews/Competitions/Competitions.vue'
                        ),
                },
                children: [
                    {
                        path:
                            routesList.competitionsPage.children
                                .SearchCompetitions.path,
                        components: {
                            'competition-router': () =>
                                import(
                                    '@/views/MainViews/Competitions/SearchCompetitions.vue'
                                ),
                        },
                    },
                    {
                        path:
                            routesList.competitionsPage.children
                                .CurrentCompetitions.path,
                        components: {
                            'competition-router': () =>
                                import(
                                    '@/views/MainViews/Competitions/CurrentCompetitions.vue'
                                ),
                        },
                        props: {
                            'competition-router': true,
                        },
                    },
                ],
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.mainQuestPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/MainQuest.vue'),
                },
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.raitingPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Raiting.vue'),
                },
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.shopPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Shop/Shop.vue'),
                },
                children: [
                    {
                        path: routesList.shopPage.children.shopItems.path,
                        components: {
                            'shop-router': () =>
                                import('@/views/MainViews/Shop/ShopItems.vue'),
                        },
                    },
                    {
                        path: routesList.shopPage.children.shopItem.path,
                        components: {
                            'shop-router': () =>
                                import('@/views/MainViews/Shop/ShopItem.vue'),
                        },
                        props: {
                            'shop-router': true,
                        },
                    },
                    {
                        path: routesList.shopPage.children.shopCart.path,
                        components: {
                            'shop-router': () =>
                                import('@/views/MainViews/Shop/ShopCart.vue'),
                        },
                    },
                ],
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.statisticsPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Statistics.vue'),
                },
                meta: {
                    requiersAuthentication: true,
                },
            },
            {
                path: routesList.testsPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Tests/Tests.vue'),
                },
                children: [
                    {
                        path: routesList.testsPage.children.testsList.path,
                        components: {
                            'tests-router': () =>
                                import('@/views/MainViews/Tests/TestsList.vue'),
                        },
                    },
                    {
                        path: routesList.testsPage.children.testPage.path,
                        components: {
                            'tests-router': () =>
                                import(
                                    '@/views/MainViews/Tests/OpenedTest.vue'
                                ),
                        },
                        props: {
                            'tests-router': true,
                        },
                    },
                ],
                meta: {
                    requiersAuthentication: true,
                },
            },
        ],
    },
    {
        path: routesList.authPage.path,
        component: () => import('@/views/Auth.vue'),
        children: [
            {
                path: routesList.authPage.children.loginPage.path,
                components: {
                    'auth-router': LoginForm,
                },
                meta: {
                    requiersToBeLoggedOut: true,
                },
            },
            {
                path: routesList.authPage.children.forgotpasswordPage.path,
                components: {
                    'auth-router': ForgotPassword,
                },
                meta: {
                    requiersToBeLoggedOut: true,
                },
            },
        ],
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiersToBeLoggedOut)) {
        if (store.getters['tokens/isAuthenticated']) {
            next(routesList.mainPage.path)
        } else {
            next()
        }
    } else {
        next()
    }

    if (to.matched.some(record => record.meta.requiersAuthentication)) {
        if (!store.getters['tokens/isAuthenticated']) {
            next(routesList.authPage.children.loginPage.path)
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router
