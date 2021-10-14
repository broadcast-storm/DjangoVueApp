<template>
    <div class="wrapper">
        <main class="main">
            <div class="rating-menu">
                <div class="command-type">
                    <a
                        class="command-type-link"
                        :class="{
                            'command-type-link__active':
                                showIndividualRating === true,
                        }"
                        @click="showIndividualRating = true"
                        >Индивидуальный</a
                    >
                    <a
                        class="command-type-link"
                        :class="{
                            'command-type-link__active':
                                showIndividualRating === false,
                        }"
                        @click="showIndividualRating = false"
                        >Командный</a
                    >
                </div>
                <div class="period">
                    <span class="period__arrow">
                        <PeriodArrowSvg class="period__arrow__svg" />
                    </span>
                    <p class="period__info">за неделю</p>
                    <span class="period__arrow">
                        <PeriodArrowSvg class="period__arrow__svg to-right" />
                    </span>
                </div>
            </div>
            <RatingList
                v-if="showIndividualRating"
                :ratings="individualRaiting"
            />
            <RatingList v-else :ratings="teamRaiting" />
        </main>
    </div>
</template>

<script>
import PeriodArrowSvg from '@/assets/icons/raiting/period-arrow.svg'
import RatingList from '@/components/Rating/RatingList'
import { mapGetters } from 'vuex'

export default {
    name: 'Raiting',
    components: { PeriodArrowSvg, RatingList },
    data() {
        return {
            showIndividualRating: true,
        }
    },
    computed: {
        ...mapGetters('raiting', [
            'getIndividRaiting',
            'getTeamRaiting',
            'getIsLoading',
        ]),
        individualRaiting: function() {
            return this.getIndividRaiting
        },
        teamRaiting: function() {
            return this.getTeamRaiting
        },
        isLoading: function() {
            return this.getIsLoading
        },
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    width: 100%;
    min-height: 100vh;
}

.main {
    padding-top: 90px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
}
.rating-menu {
    padding: 25px 70px;
    display: flex;
    justify-content: space-between;
    .command-type {
        width: 420px;
        display: flex;
        justify-content: space-between;
        color: #545969;
        font-size: 24px;
        .command-type-link {
            padding-bottom: 8px;
            color: #545969;
            text-decoration: none;
            cursor: pointer;
        }
        .command-type-link__active {
            border-bottom: 2px solid #545969;
        }
    }
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
</style>
