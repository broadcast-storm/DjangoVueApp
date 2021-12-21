<template>
    <div class="wrapper">
        <main class="main">
            <div class="wrap-info-right">
                <div class="rating-wrap">
                    <h3 class="individual-rating">Индивидуальный рейтинг</h3>
                    <div class="period">
                        <span class="period__arrow">
                            <PeriodArrowSvg class="period__arrow__svg" />
                        </span>
                        <p class="period__info">за неделю</p>
                        <span class="period__arrow">
                            <PeriodArrowSvg
                                class="period__arrow__svg to-right"
                            />
                        </span>
                    </div>
                </div>

                <!-- БЛОК ИНДИВИДУАЛЬНОГО РЕЙТИНГА -->
                <div class="b-right">
                    <div
                        v-for="rating in individualRating"
                        :key="rating.id"
                        class="b-right__item"
                    >
                        <div class="b-right__num">{{ rating.id }}</div>
                        <div class="b-right__info">
                            <img
                                class="b-right__img"
                                :src="rating.img"
                                alt=""
                            />
                            <div class="b-right__wrap">
                                <h4 class="b-right__title">
                                    {{ rating.name }}
                                </h4>
                                <span class="b-right__description">{{
                                    rating.description
                                }}</span>
                                <p class="b-right__rating">
                                    Рейтинг
                                    {{ toNumberString(rating.ratingValue) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- БЛОК КОМАНДНОГО РЕЙТИНГА -->
            <div class="wrap-info-right">
                <div class="rating-wrap">
                    <h3 class="individual-rating">Командный рейтинг</h3>
                    <div class="period">
                        <span class="period__arrow">
                            <PeriodArrowSvg class="period__arrow__svg" />
                        </span>
                        <p class="period__info">за месяц</p>
                        <span class="period__arrow">
                            <PeriodArrowSvg
                                class="period__arrow__svg to-right"
                            />
                        </span>
                    </div>
                </div>

                <div class="b-left">
                    <div
                        v-for="rating in teamRating"
                        :key="rating.id"
                        class="b-left__item"
                    >
                        <div class="b-left__num">{{ rating.id }}</div>
                        <div class="b-left__info">
                            <img class="b-left__img" :src="rating.img" alt="" />
                            <div class="b-left__wrap">
                                <h4 class="b-left__title">
                                    {{ rating.name }}
                                </h4>
                                <p class="b-left__rating">
                                    Рейтинг
                                    {{ toNumberString(rating.ratingValue) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import PeriodArrowSvg from '@/assets/icons/rating/period-arrow.svg'

import { mapGetters } from 'vuex'

export default {
    name: 'Rating',
    components: { PeriodArrowSvg },
    props: {},
    computed: {
        ...mapGetters('rating', [
            'getIndividRating',
            'getTeamRating',
            'getIsLoading',
        ]),
        individualRating: function() {
            return this.getIndividRating
        },
        teamRating: function() {
            return this.getTeamRating
        },
        isLoading: function() {
            return this.getIsLoading
        },
    },
    methods: {
        toNumberString: function(num) {
            if (Number.isInteger(num)) {
                return num + '.00'
            } else {
                return num.toFixed(2).toString()
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    height: 100vh;
}

.main {
    padding-top: 90px;
    display: flex;
    justify-content: space-between;
    height: 100%;
    box-sizing: border-box;
}

.wrap-info-right {
    width: 100%;
    margin-left: 70px;
    margin-right: 14px;
    /* max-height: calc(100vh - 163px);
     */
    height: 100%;
    overflow-y: auto;
}

.individual-rating {
    margin: 17px 0 5px 0;
    font-size: 24px;
    color: #545969;
}

.period {
    display: flex;
    align-items: center;
    &__info {
        font-size: 24px;
        margin: 0 8px;
        color: #7d849a;
    }

    &__arrow {
        display: flex;
        align-items: center;
        &__svg {
            width: 10px;
        }
        .to-right {
            transform: scale(-1, 1);
        }
        &:hover {
            opacity: 0.3;
        }
    }
}

.b-right {
    &__item {
        display: flex;
        max-height: 88px;
        max-width: 448px;
        margin: 24px 0;
        background: #fff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    }

    &__num {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #26bcc2;
        color: #fff;
        font-size: 64px;
        width: 72px;
        height: 88px;
    }

    &__info {
        display: flex;
        flex: 1;
        padding: 5px;
        padding-left: 8px;
    }

    &__img {
        max-width: 81px;
        max-height: 78px;
        margin-right: 11px;
    }

    &__title,
    &__rating {
        font-size: 18px;
        line-height: 16px;
        color: #7d849a;
    }

    &__title {
        color: #1a2740;
    }

    &__description {
        font-size: 12px;
        line-height: 25px;
        color: #7d849a;
    }

    &__rating {
        margin-top: 7px;
    }
}

.b-left {
    &__item {
        display: flex;
        max-height: 88px;
        max-width: 448px;
        margin: 24px 0;
        background: #fff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    }

    &__num {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #26bcc2;
        color: #fff;
        font-size: 64px;
        width: 72px;
        height: 88px;
    }

    &__info {
        display: flex;
        flex: 1;
        padding: 5px;
        padding-left: 8px;
    }

    &__img {
        max-width: 81px;
        max-height: 78px;
        margin-right: 11px;
    }

    &__title,
    &__rating {
        font-size: 18px;
        line-height: 16px;
        color: #7d849a;
    }

    &__title {
        color: #1a2740;
    }

    &__rating {
        margin-top: 27px;
    }
}
</style>
