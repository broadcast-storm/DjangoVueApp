<template>
    <div id="app">
        <router-view />
    </div>
</template>

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
