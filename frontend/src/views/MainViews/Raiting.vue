<template>
    <div class="wrapper">
        <main class="main">
            <div class="rating-menu">
                <div class="command-type">
                    <!-- <h3 class='selected'>Индивидуальный</h3> -->
                    <router-link to="/individual">Индивидуальный</router-link>
                    <router-link to="/command">Командный</router-link>
                    <!-- <h3>Командный</h3> -->
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
            <router-view></router-view>
            <!-- БЛОК ИНДИВИДУАЛЬНОГО РЕЙТИНГА -->
            <div class="rating-table">
                <div class="row-individual">
                    <div
                        v-for="raiting in individualRaiting"
                        :key="raiting.id"
                        class="row-individual__item"
                    >
                        <div class="row-individual__num">{{ raiting.id }}</div>
                        <div class="row-individual__info">
                            <img
                                class="row-individual__img"
                                :src="raiting.img"
                                alt=""
                            />
                            <div class="row-individual__wrap">
                                <h4 class="row-individual__title">
                                    {{ raiting.name }}
                                </h4>
                                <span class="row-individual__description"
                                    >Отдел: {{ raiting.description }}</span
                                >
                                <p class="row-individual__raiting">
                                    Рейтинг
                                    {{ toNumberString(raiting.raitingValue) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- БЛОК КОМАНДНОГО РЕЙТИНГА -->
            <div class="rating-table">
                <div class="row-command">
                    <div
                        v-for="raiting in teamRaiting"
                        :key="raiting.id"
                        class="row-command__item"
                    >
                        <div class="row-command__num">{{ raiting.id }}</div>
                        <div class="row-command__info">
                            <img
                                class="row-command__img"
                                :src="raiting.img"
                                alt=""
                            />
                            <div class="row-command__wrap">
                                <h4 class="row-command__title">
                                    {{ raiting.name }}
                                </h4>
                                <p class="row-command__raiting">
                                    Рейтинг
                                    {{ toNumberString(raiting.raitingValue) }}
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
import PeriodArrowSvg from '@/assets/icons/raiting/period-arrow.svg'
import { mapGetters } from 'vuex'

const individual = {
    template: `
    <div class="rating-table">
                <div class="row-individual">
                    <div
                        v-for="raiting in individualRaiting"
                        :key="raiting.id"
                        class="row-individual__item"
                    >
                        <div class="row-individual__num">{{ raiting.id }}</div>
                        <div class="row-individual__info">
                            <img
                                class="row-individual__img"
                                :src="raiting.img"
                                alt=""
                            />
                            <div class="row-individual__wrap">
                                <h4 class="row-individual__title">
                                    {{ raiting.name }}
                                </h4>
                                <span class="row-individual__description">Отдел: {{
                                    raiting.description
                                }}</span>
                                <p class="row-individual__raiting">
                                    Рейтинг
                                    {{ toNumberString(raiting.raitingValue) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    `,
}
const command = {
    template: `
    <div class="rating-table">
                <div class="row-command">
                    <div
                        v-for="raiting in teamRaiting"
                        :key="raiting.id"
                        class="row-command__item"
                    >
                        <div class="row-command__num">{{ raiting.id }}</div>
                        <div class="row-command__info">
                            <img
                                class="row-command__img"
                                :src="raiting.img"
                                alt=""
                            />
                            <div class="row-command__wrap">
                                <h4 class="row-command__title">
                                    {{ raiting.name }}
                                </h4>
                                <p class="row-command__raiting">
                                    Рейтинг
                                    {{ toNumberString(raiting.raitingValue) }}
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    `,
}

const routes = [
    { path: '/', component: individual },
    { path: '/command', component: command },
]
routes
export default {
    name: 'Raiting',
    components: { PeriodArrowSvg },
    props: {},
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
        h3 {
            padding-bottom: 10px;
        }
        .selected {
            border-bottom: 3px solid #545969;
        }
    }
}
.rating-table {
    margin-left: 70px;
    margin-right: 14px;
    // height: 100%;
    // overflow-y: auto;
    .row-individual__item:nth-child(1) {
        .row-individual__num {
            background-color: #ebe31d;
        }
    }
    .row-individual__item:nth-child(2) {
        .row-individual__num {
            background-color: #99a4a5;
        }
    }
    .row-individual__item:nth-child(3) {
        .row-individual__num {
            background-color: #be8e10;
        }
    }
    .row-command__item:nth-child(1) {
        .row-command__num {
            background-color: #ebe31d;
        }
    }
    .row-command__item:nth-child(2) {
        .row-command__num {
            background-color: #99a4a5;
        }
    }
    .row-command__item:nth-child(3) {
        .row-command__num {
            background-color: #be8e10;
        }
    }
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

.row-individual {
    &__item {
        display: flex;
        max-height: 88px;
        max-width: 75%;
        margin: 17px 0;
        background: #fff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    }

    &__num {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #26bcc2;
        color: #fff;
        font-size: 48px;
        width: 81px;
        height: 88px;
    }

    &__info {
        display: flex;
        flex: 1;
        // padding: 5px;
        // padding-left: 8px;
    }

    &__img {
        // max-width: 81px;
        // max-height: 78px;
        margin-right: 11px;
    }

    &__title,
    &__raiting {
        font-size: 18px;
        line-height: 16px;
        color: #7d849a;
    }

    &__title {
        padding-top: 8px;
        color: #1a2740;
    }
    &__description {
        font-size: 12px;
        line-height: 25px;
        color: #7d849a;
    }

    &__raiting {
        margin-top: 7px;
    }
}
.row-command {
    &__item {
        display: flex;
        max-height: 88px;
        max-width: 75%;
        margin: 17px 0;
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
        width: 81px;
        height: 88px;
    }

    &__info {
        display: flex;
        flex: 1;
        // padding: 5px;
        // padding-left: 8px;
    }

    &__img {
        // max-width: 81px;
        // max-height: 78px;
        margin-right: 11px;
    }

    &__title,
    &__raiting {
        font-size: 18px;
        line-height: 16px;
        color: #7d849a;
    }

    &__title {
        padding-top: 8px;
        color: #1a2740;
    }

    &__description {
        font-size: 12px;
        line-height: 25px;
        color: #7d849a;
    }

    &__raiting {
        margin-top: 35px;
    }
}
</style>
