<template>
    <div
        class="logo-container"
        :class="{ canBeActive }"
        @mouseover="mouseOver"
        @mouseleave="mouseLeave"
    >
        <simple-svg
            :src="svgSrc"
            :fill="svgFillColor()"
            fill-class-name="fill-to-change"
            :stroke="svgFillColor()"
            stroke-class-name="stroke-to-change"
            width="100%"
            height="100%"
            custom-id="logoId"
            custom-class-name="logo-svg"
            @load="svgLoaded()"
        />
    </div>
</template>

<script>
export default {
    name: 'LogoSvg',
    props: {
        regularColor: {
            type: String,
            default: '#26bcc2',
        },
        activeColor: {
            type: String,
            default: '#26bcc2',
        },
        canBeActive: {
            type: Boolean,
            default: false,
        },
    },
    data() {
        return {
            isActive: false,
            regularFill: this.regularColor,
            activeFill: this.activeColor,
            svgSrc: require('@/assets/icons/logo.svg'),
        }
    },
    methods: {
        svgFillColor() {
            return this.isActive ? this.activeFill : this.regularFill
        },
        mouseOver() {
            if (this.canBeActive) this.isActive = true
        },
        mouseLeave() {
            if (this.canBeActive) this.isActive = false
        },
        svgLoaded() {
            console.log('Logo is loaded!')
        },
    },
}
</script>

<style lang="scss" scoped>
.logo-container {
    width: 150px;
}
.canBeActive {
    cursor: pointer;
}
</style>
