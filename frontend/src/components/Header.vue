<template>
    <div class="header-container">
        <h1 class="header-container__page-name">Профиль</h1>
        <div class="user-statistics">
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
export default {
    name: 'Header',
    components: { CoinSvg, HeartSvg, LightningSvg },
    props: {
        statistics: {
            type: Object,
            required: true,
        },
    },
}
</script>

<style lang="scss" scoped>
.header-container {
    display: flex;
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
}
</style>
