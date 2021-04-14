<template>
    <div class="main-container">
        <Header :statistics="stats" />
        <Navbar />
        <div class="main-container__content">
            <router-view name="main-router" />
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header'
import Navbar from '@/components/Navbar/Navbar'
import { mapGetters } from 'vuex'

import routesList from '@/router/routesList'
import { mapActions } from 'vuex'
import { AUTH_LOGOUT } from '@/store/action-types/tokens'

export default {
    name: 'Main',
    components: { Header, Navbar },
    data() {
        return {}
    },
    onIdle() {
        this.AUTH_LOGOUT().then(() => {
            this.$router.push(routesList.authPage.children.loginPage.path)
        })
    },
    computed: {
        ...mapGetters(['getUserData']),
        stats: function() {
            return this.getUserData.stats
        },
    },
    methods: {
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
