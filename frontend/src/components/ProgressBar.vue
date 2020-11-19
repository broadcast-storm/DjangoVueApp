<template>
    <div class="progressbar">
        <span class="progressbar__value">{{ percent }}%</span>
        <div :style="{ width: percent + '%' }" class="progressbar__bar"></div>
    </div>
</template>

<script>
export default {
    name: 'ProgressBar',
    props: {
        percent: {
            type: Number,
            default: 0,
        },
    },
}
</script>

<style lang="scss" scoped>
.progressbar {
    width: 100%;
    height: 16px;
    background-color: #d8dcea;
    position: relative;
    border-radius: 16px;
    display: flex;
    padding-left: 15px;
    align-items: center;
    box-sizing: border-box;

    &__value {
        font-size: 12px;
        z-index: 2;
    }

    &__bar {
        height: 100%;
        background-color: $progressbar-color;
        position: absolute;
        top: 0;
        left: 0px;
        border-radius: 16px;
        z-index: 1;
    }
}
</style>
