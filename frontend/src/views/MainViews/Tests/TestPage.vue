<template>
    <div class="tests-wrapper">
        ssss
    </div>
</template>

<script>
export default {
    props: {
        id: {
            default: '0',
            type: String,
        },
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.tests-wrapper {
    display: flex;
    flex-direction: row;
    margin-top: 90px;
    height: calc(100vh - 90px);
    flex-wrap: wrap;
    width: 100%;
    overflow-y: auto;
}
</style>
