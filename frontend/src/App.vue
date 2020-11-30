<template>
    <div id="app">
        <LoadingPopup v-if="isFirstRefreshing" />
        <router-view v-else />
    </div>
</template>

<script>
import LoadingPopup from '@/components/LoadingPopup'
import { AUTH_REFRESH_REQUEST } from '@/store/action-types/tokens'
import routesList from '@/router/routesList'
import { mapState, mapActions, mapGetters } from 'vuex'

export default {
    components: { LoadingPopup },
    data() {
        return {
            isFirstRefreshing: false,
            timerId: null,
        }
    },
    computed: {
        ...mapState({
            firstRequestSuccess: state => state.tokens.firstRequestSuccess,
        }),
        ...mapGetters('tokens', ['isAuthenticated']),
    },
    watch: {
        firstRequestSuccess(newValue, oldValue) {
            var self = this
            var timeToRefresh =
                parseInt(process.env.VUE_APP_ACCESS_TOKEN_EXPIRES) * 60 * 1000 -
                30 * 1000

            if (newValue && !oldValue) {
                console.log(`user signed in`)
                self.timerId = setTimeout(async function tick() {
                    await self.AUTH_REFRESH_REQUEST()
                    console.log(`refresh access token`)
                    self.timerId = setTimeout(tick, timeToRefresh)
                }, timeToRefresh)
            }

            if (!newValue && oldValue) {
                clearTimeout(this.timerId)
            }
        },
    },
    async mounted() {
        await this.refreshTokenOnMount()
    },
    methods: {
        ...mapActions('tokens', [AUTH_REFRESH_REQUEST]),
        async refreshTokenOnMount() {
            try {
                if (this.isAuthenticated) {
                    this.isFirstRefreshing = true
                    await this.AUTH_REFRESH_REQUEST()
                    this.isFirstRefreshing = false
                }
            } catch (error) {
                console.log(error)
                this.$router.push(
                    routesList.authPage.children.loginPage.path,
                    () => (this.isFirstRefreshing = false)
                )
            }
        },
    },
}
</script>

<style lang="scss">
* {
    margin: 0;
    padding: 0;
    font-family: Helvetica;
    font-style: normal;
    font-weight: normal;
}
html {
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}
@media (max-width: $media-breakpoint-sm) {
    * {
        font-family: Gerbera;
        font-style: normal;
        font-weight: normal;
    }
}
</style>
