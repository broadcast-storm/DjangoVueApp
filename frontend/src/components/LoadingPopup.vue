<template>
    <div class="popup">
        <div class="popup__container">
            <LogoSvg
                class="popup__container__logo"
                :regular-color="'#26bcc2'"
            />
            <Spinner
                :size="25"
                :line-bg-color="'#b1b2b7'"
                :line-fg-color="'#26bcc2'"
            />
        </div>
    </div>
</template>

<script>
import LogoSvg from '@/components/LogoSvg'
import Spinner from 'vue-simple-spinner'

export default {
    name: 'LoadingPopup',
    components: { LogoSvg, Spinner },
}
</script>

<style lang="scss" scoped>
.popup {
    background-color: $basic-grey;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    &__container {
        width: 200px;
        display: flex;
        justify-content: center;
        flex-direction: column;
        &__logo {
            width: 100%;
            margin-bottom: 10px;
        }
    }
}

@media (max-width: $media-breakpoint-md) {
    .popup {
        &__container {
            width: 100px;
        }
    }
}
</style>
