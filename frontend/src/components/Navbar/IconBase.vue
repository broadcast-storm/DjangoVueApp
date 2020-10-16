<template>
    <div :style="`width:${width}px; height:${height}px`" @click="onClick">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            :viewBox="`0 0 ${viewBoxWidth} ${viewBoxHeight}`"
        >
            <g :fill="fillColor" :stroke="strokeColor">
                <slot />
            </g>
        </svg>
    </div>
</template>

<script>
export default {
    props: {
        width: {
            type: Number,
            default: 30,
        },
        height: {
            type: Number,
            default: 30,
        },
        viewBoxWidth: {
            type: Number,
            default: 30,
        },
        viewBoxHeight: {
            type: Number,
            default: 30,
        },
        fillColor: {
            type: String,
            default: 'currentColor',
        },
        strokeColor: {
            type: String,
            default: 'currentColor',
        },
        onClick: {
            type: Function,
            default: () => {},
        },
    },
}
</script>

<style lang="scss">
div {
    svg {
        width: 100%;
        height: 100%;
    }
}
</style>
