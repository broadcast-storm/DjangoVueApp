<template>
    <div class="main-container">
        <Header :statistics="profileStats" />
        <Navbar />
        <div class="main-container__content">
            <router-view
                v-if="profileStats.status === 'success'"
                name="main-router"
            />
            <LoadingPopup v-else />
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header'
import LoadingPopup from '@/components/LoadingPopup'
import Navbar from '@/components/Navbar/Navbar'
import { mapGetters, mapActions } from 'vuex'
import routesList from '@/router/routesList'
import { AUTH_LOGOUT } from '@/store/action-types/tokens'
import { PROFILE_REQUEST_FETCHING } from '@/store/action-types/profile'

export default {
    name: 'Main',
    components: { Header, Navbar, LoadingPopup },
    data() {
        return {}
    },
    onIdle() {
        this.AUTH_LOGOUT().then(() => {
            this.$router.push(routesList.authPage.children.loginPage.path)
        })
    },
    computed: {
        ...mapGetters('profile', ['profileStats']),
    },
    async mounted() {
        await this.PROFILE_REQUEST_FETCHING()
    },
    methods: {
        ...mapActions('profile', [PROFILE_REQUEST_FETCHING]),
        ...mapActions('tokens', [AUTH_LOGOUT]),
    },
}
</script>

<style lang="scss">
.main-container {
    box-sizing: content-box;
    width: 100%;
    min-width: 1023px;
    background-color: $basic-grey;
    &__content {
        margin-left: 90px;
    }
}
@media (max-width: $media-breakpoint-sm) {
    .main-container {
        min-width: auto;
        &__content {
            margin-left: 0;
        }
    }
}
</style>
