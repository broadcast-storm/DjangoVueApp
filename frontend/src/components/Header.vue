<template>
    <div class="header-container">
        <h1 class="header-container__page-name">
            {{ pageName }}
        </h1>
        <div
            class="user-statistics"
            :class="{
                hidden: $router.currentRoute.path === '/',
            }"
        >
            <div class="user-statistics__stat-block">
                <CoinSvg class="user-statistics__icon" />
                <span
                    class="user-statistics__text user-statistics__text_color_yellow"
                    >{{ statistics.coins }}</span
                >
            </div>
            <div class="user-statistics__stat-block">
                <LightningSvg class="user-statistics__icon" />
                <span
                    class="user-statistics__text user-statistics__text_color_green"
                    >{{ statistics.lightnings }}</span
                >
            </div>
            <div class="user-statistics__stat-block">
                <HeartSvg class="user-statistics__icon" />
                <span
                    class="user-statistics__text user-statistics__text_color_red"
                    >{{ statistics.hearts }}</span
                >
            </div>
        </div>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import HeartSvg from '@/assets/icons/heart.svg'
import LightningSvg from '@/assets/icons/lightning.svg'
import routesList from '@/router/routesList'

export default {
    name: 'Header',
    components: { CoinSvg, HeartSvg, LightningSvg },
    props: {
        statistics: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            routesList,
            pageName: '',
        }
    },

    watch: {
        $route(to) {
            this.getPageName(to.fullPath)
        },
    },

    mounted() {
        this.getPageName(this.$router.currentRoute.fullPath)
    },

    methods: {
        getPageName(currentPath) {
            for (var page in this.routesList) {
                const currentRoute = `/${currentPath.split('/')[1]}`
                if (this.routesList[page].path === currentRoute) {
                    this.pageName = this.routesList[page].header
                }
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.header-container {
    background-color: $basic-grey;
    width: 100%;
    position: fixed;
    z-index: 1000;
    right: 0;
    top: 0;
    display: flex;
    box-sizing: border-box;
    justify-content: space-between;
    align-items: center;
    padding: 30px 90px;
    border: 1px solid #b1b2b7;
    &__page-name {
        font-size: 24px;
        line-height: 28px;
        color: $brand-night;
    }

    .user-statistics {
        display: flex;
        &__stat-block {
            display: flex;
            align-items: center;
            margin-left: 60px;
        }
        &__icon {
            width: 20px;
            height: 20px;
        }
        &__text {
            font-size: 16px;
            line-height: 16px;
            color: #f2af49;
            margin-left: 5px;

            &_color {
                &_red {
                    color: $text-color-red;
                }
                &_yellow {
                    color: $text-color-yellow;
                }
                &_green {
                    color: $text-color-green;
                }
            }
        }
    }

    .hidden {
        visibility: hidden;
    }
}

@media (max-width: $media-breakpoint-md) {
    .header-container {
        padding: 25px 90px;
        &__page-name {
            font-size: 20px;
        }

        .user-statistics {
            &__stat-block {
                margin-left: 20px;
            }
            &__icon {
                width: 20px;
            }
            &__text {
                font-size: 16px;
                line-height: 16px;
            }
        }
    }
}

@media (max-width: $media-breakpoint-sm) {
    .header-container {
        position: absolute;
        flex-direction: column-reverse;
        padding: 0;
        border: none;
        &__page-name {
            margin-top: 16px;
            font-size: 18px;
        }

        .user-statistics {
            width: 100%;
            height: 36px;
            padding: 10px 0;
            justify-content: space-around;
            align-items: center;
            box-shadow: 0px 6px 4px rgba(0, 0, 0, 0.1);
            &__stat-block {
                margin: 0;
            }
            &__icon {
                width: 20px;
            }
            &__text {
                font-size: 16px;
                line-height: 16px;
            }
        }
        .hidden {
            visibility: visible;
        }
    }
}
</style>
