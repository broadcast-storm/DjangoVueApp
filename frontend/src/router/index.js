import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main'
import LoginForm from '@/views/AuthViews/LoginForm'
import ForgotPassword from '@/views/AuthViews/ForgotPassword'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Main',
        component: Main,
        children: [
            {
                path: '/',
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Profile.vue'),
                },
            },
            {
                path: '/competitions',
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Competitions.vue'),
                },
            },
            {
                path: '/main-quest',
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/MainQuest.vue'),
                },
            },
            {
                path: '/raiting',
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Raiting.vue'),
                },
            },
            {
                path: '/shop',
                components: {
                    'main-router': () => import('@/views/MainViews/Shop.vue'),
                },
            },
            {
                path: '/statistics',
                components: {
                    'main-router': () =>
                        import('@/views/MainViews/Statistics.vue'),
                },
            },
            {
                path: '/tests',
                components: {
                    'main-router': () => import('@/views/MainViews/Tests.vue'),
                },
            },
        ],
    },
    {
        path: '/auth',
        name: 'Auth',
        component: () => import('@/views/Auth.vue'),
        children: [
            {
                path: 'login',
                components: {
                    'auth-router': LoginForm,
                },
            },
            {
                path: 'forgot-password',
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
