<template>
    <div id="app">
        <LoadingPopup v-if="$store.state.tokens.status === 'refreshing'" />
        <router-view v-else />
    </div>
</template>

<script>
import LoadingPopup from '@/components/LoadingPopup'
import { AUTH_REFRESH_REQUEST } from '@/store/actions/tokens'

export default {
    components: { LoadingPopup },
    async mounted() {
        try {
            if (this.$store.getters.isAuthenticated)
                await this.$store.dispatch(AUTH_REFRESH_REQUEST)
        } catch (error) {
            console.log(error)
        }
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
