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
                        import('@/views/MainViews/Competitions.vue'),
                },
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
                    'main-router': () => import('@/views/MainViews/Shop.vue'),
                },
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
                    'main-router': () => import('@/views/MainViews/Tests.vue'),
                },
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
        if (store.getters.isAuthenticated) {
            next(routesList.mainPage.path)
        } else {
            next()
        }
    } else {
        next()
    }

    if (to.matched.some(record => record.meta.requiersAuthentication)) {
        if (!store.getters.isAuthenticated) {
            next(routesList.authPage.children.loginPage.path)
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router
