import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import LoginForm from '@/views/AuthViews/LoginForm'
import ForgotPassword from '@/views/AuthViews/ForgotPassword'
import routesList from '@/router/routesList'

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
            },
            {
                path: routesList.competitionsPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Competitions.vue'),
                },
            },
            {
                path: routesList.mainQuestPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/MainQuest.vue'),
                },
            },
            {
                path: routesList.raitingPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Raiting.vue'),
                },
            },
            {
                path: routesList.shopPage.path,
                components: {
                    'main-router': () => import('@/views/MainViews/Shop.vue'),
                },
            },
            {
                path: routesList.statisticsPage.path,
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Statistics.vue'),
                },
            },
            {
                path: routesList.testsPage.path,
                components: {
                    'main-router': () => import('@/views/MainViews/Tests.vue'),
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
            },
            {
                path: routesList.authPage.children.forgotpasswordPage.path,
                components: {
                    'auth-router': ForgotPassword,
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

export default router
