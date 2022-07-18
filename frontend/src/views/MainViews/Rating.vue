<template>
    <div class="wrapper">
        <main class="main">
            <div class="rating-menu">
                <div class="command-type">
                    <div
                        class="command-type__tab"
                        :class="{
                            'command-type__tab-active': showIndividualRating,
                        }"
                        @click="showIndividualRating = true"
                    >
                        <Union class="union-icon" />
                        Индивидуальный
                    </div>
                    <div
                        :class="{
                            'command-type__triangle-right': showIndividualRating,
                            'command-type__triangle-left': !showIndividualRating,
                        }"
                    ></div>
                    <div
                        class="command-type__tab"
                        :class="{
                            'command-type__tab-active': !showIndividualRating,
                        }"
                        @click="showIndividualRating = false"
                    >
                        <Group class="group-icon" />
                        Командный
                    </div>
                </div>
                <div class="rating-sort">
                    Показать за:
                    <div
                        class="selected-method"
                        @click="showSelection = !showSelection"
                    >
                        {{ getCurrentSortMethod
                        }}<ArrowDown class="arrow-icon" />
                    </div>
                </div>
                <div v-if="showSelection" class="selection">
                    <div
                        class="selection-method"
                        @click="
                            currentSortMethod = 'day'
                            showSelection = !showSelection
                        "
                    >
                        день
                    </div>
                    <div
                        class="selection-method"
                        @click="
                            currentSortMethod = 'week'
                            showSelection = !showSelection
                        "
                    >
                        неделя
                    </div>
                    <div
                        class="selection-method"
                        @click="
                            currentSortMethod = 'month'
                            showSelection = !showSelection
                        "
                    >
                        месяц
                    </div>
                </div>
            </div>
            <RatingList
                v-if="showIndividualRating"
                :ratings="individualRating"
                :sort="currentSortMethod"
            />
            <RatingList
                v-else
                :ratings="teamRating"
                :sort="currentSortMethod"
            />
        </main>
    </div>
</template>

<script>
import RatingList from '@/components/Rating/RatingList'
import Group from '@/assets/icons/rating/group.svg'
import Union from '@/assets/icons/rating/union.svg'
import ArrowDown from '@/assets/icons/rating/arrow-down.svg'
import { mapGetters } from 'vuex'

export default {
    name: 'Rating',
    components: { RatingList, Group, Union, ArrowDown },
    data() {
        return {
            showIndividualRating: true,
            showSelection: false,
            currentSortMethod: 'month',
        }
    },
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
        getCurrentSortMethod: function() {
            let c
            switch (this.currentSortMethod) {
                case 'day':
                    c = 'день'
                    break
                case 'week':
                    c = 'неделя'
                    break
                case 'month':
                    c = 'месяц'
                    break
            }
            return c
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
    flex-direction: column;
    display: flex;
    justify-content: space-between;
    .command-type {
        width: 585px;
        display: flex;
        color: #545969;
        font-size: 24px;
        border: 1px solid #545969;
        box-sizing: border-box;
        margin-bottom: 19px;
        &__tab {
            font-weight: bold;
            font-size: 24px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 68px;
            padding-right: 25px;
            padding-left: 25px;
            cursor: pointer;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            .union-icon {
                width: 25px;
                position: relative;
                top: 3.5px;
                margin-right: 14px;
                path {
                    fill: #000;
                }
            }
            .group-icon {
                width: 42px;
                margin-right: 14px;
            }
        }
        &__triangle-right {
            width: 0;
            height: 0;
            border-top: 68px solid #545969;
            border-right: 36px solid transparent;
        }
        &__triangle-left {
            width: 0;
            height: 0;
            border-bottom: 68px solid #545969;
            border-left: 36px solid transparent;
        }
        &__tab-active {
            background: #545969;
            color: #dee2f4;
        }
    }
    .rating-sort {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        font-size: 18px;
        color: #545969;
        .selected-method {
            background: #ffffff;
            box-shadow: inset 0px -2px 5px rgba(0, 0, 0, 0.25);
            border-radius: 10px;
            padding: 9px 14px 9px 23px;
            color: #6a6d76;
            margin-left: 11px;
            cursor: pointer;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            .arrow-icon {
                height: 12px;
                width: 20px;
                margin-left: 16px;
            }
        }
    }
    .selection {
        transform:translate3d(120px, 130px, 0px);
        position: absolute;
        background: #ffffff;
        color: #6a6d76;
        width: 120px;

        &-method {
            font-size: 18px;
            padding-left: 23px;
            cursor: pointer;
            margin: 5px 0px;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
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
