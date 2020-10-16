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
import { stats } from '@/mocks/headerStats'
export default {
    name: 'Main',
    components: { Header, Navbar },
    data() {
        return {
            stats,
        }
    },
}
</script>

<style lang="scss">
.main-container {
    box-sizing: border-box;
    width: 100%;
    min-height: 100vh;
    background-color: $basic-grey;
    &__content {
        margin-left: 90px;
    }
}
</style>
