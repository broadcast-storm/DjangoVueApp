<template>
    <div class="wrapper">
        <main class="main">
            <div class="statistics">
                <div class="statistics__main">
                    <div class="statistics__main__item">
                        <h4 class="statistic-title">Получено ачивок:</h4>
                        <span class="statistic-result">{{
                            statistics.achievesCount
                        }}</span>
                    </div>
                    <div class="statistics__main__item">
                        <h4 class="statistic-title">Текущий уровень:</h4>
                        <span class="statistic-result">{{
                            statistics.currentLevel
                        }}</span>
                    </div>
                    <div class="statistics__main__item">
                        <h4 class="statistic-title">Дней в компании:</h4>
                        <span class="statistic-result">{{
                            statistics.daysInCompany
                        }}</span>
                    </div>
                    <div class="statistics__main__item">
                        <h4 class="statistic-title">
                            Прогресс за <br />
                            неделю:
                        </h4>
                        <span class="statistic-result"
                            >{{
                                (statistics.weekProgress * 100).toFixed()
                            }}%</span
                        >
                    </div>
                    <div class="statistics__main__item">
                        <h4 class="statistic-title">
                            Прогресс за <br />
                            месяц:
                        </h4>
                        <span class="statistic-result"
                            >{{
                                (statistics.monthProgress * 100).toFixed()
                            }}%</span
                        >
                    </div>
                </div>
                <div class="statistics__best">
                    <div class="statistics__best__header">
                        <h4 class="header-title">Лучший результат</h4>
                        <span class="header-date"
                            >за {{ statistics.bestResult.bestMonth }}
                            {{ statistics.bestResult.bestYear }}</span
                        >
                    </div>
                    <div class="statistics__best__item">
                        <h4 class="best-title">Выполнено заданий:</h4>
                        <span class="best-result">{{
                            statistics.bestResult.completedTasks
                        }}</span>
                    </div>
                    <div class="statistics__best__item">
                        <h4 class="best-title">Качество:</h4>
                        <span class="best-result"
                            >{{
                                (statistics.bestResult.quality * 100).toFixed()
                            }}%</span
                        >
                    </div>
                </div>
            </div>
            <div class="achievements">
                <h3 class="achievements__title">Полученные ачивки</h3>
                <div
                    v-for="achive in receivedAchieves"
                    :key="achive.id"
                    class="achievements__item"
                >
                    <div class="achievements__item__img-container">
                        <img
                            class="image"
                            :src="achive.img"
                            :alt="achive.title"
                        />
                    </div>
                    <div class="achievements__item__content">
                        <h4 class="achievement-title">{{ achive.title }}</h4>
                        <h4 class="achievement-title">Описание:</h4>
                        <p class="achievement-description">
                            {{ achive.description }}
                        </p>
                        <span class="achievement-date"
                            >Выполнена: {{ achive.date }}</span
                        >
                    </div>
                </div>
            </div>
            <div class="indicators">
                <h3 class="indicators__title">Показатели</h3>
                <div class="indicators__item">
                    <h4 class="indicators__category">Продуктивность</h4>
                    <div class="indicators__wrap-graph">
                        <line-chart
                            :chart-data="datacollection"
                            :height="null"
                            :width="null"
                        ></line-chart>
                    </div>
                    <span class="indicators__time-period">неделя</span>
                </div>
                <div class="indicators__item">
                    <h4 class="indicators__category">Качество</h4>
                    <div class="indicators__wrap-graph">
                        <bar-chart
                            :chart-data="datacollection2"
                            :height="null"
                            :width="null"
                        ></bar-chart>
                    </div>
                    <span class="indicators__time-period">неделя</span>
                </div>
            </div>
        </main>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'

import LineChart from '@/components/graphs/LineChart.js'
import BarChart from '@/components/graphs/BarChart.js'

export default {
    name: 'Statistics',
    components: {
        LineChart,
        BarChart,
    },
    data() {
        return {
            datacollection: null,
            datacollection2: null,
        }
    },
    computed: {
        ...mapGetters('statistics', [
            'getStatistics',
            'getReceivedAchieves',
            'getIndicators',
            'getIsLoading',
        ]),
        statistics: function() {
            return this.getStatistics
        },
        receivedAchieves: function() {
            return this.getReceivedAchieves
        },
        indicators: function() {
            return this.getIndicators
        },
        isLoading: function() {
            return this.getIsLoading
        },
    },
    mounted() {
        this.fillData()
    },
    methods: {
        fillData() {
            this.datacollection = {
                labels: ['1', '2', '3', '4', '5', '6', '7', '8'],
                datasets: [
                    {
                        label: 'Продуктивность',
                        data: [
                            118.36,
                            101.1,
                            117,
                            121.33,
                            109,
                            112,
                            113.87,
                            120.37,
                        ],
                        backgroundColor: 'transparent',
                        borderColor: '#061d4c',
                        tension: 0.1,
                        datalabels: {
                            align: 'end',
                            anchor: 'end',
                            borderColor: '#bfbfbf',
                            backgroundColor: '#ffffff',
                            borderWidth: 1,
                            borderRadius: 3,
                        },
                    },
                ],
            }
            this.datacollection2 = {
                labels: ['1', '2', '3', '4', '5', '6', '7', '8'],
                datasets: [
                    {
                        label: 'Качество',
                        data: [98.5, 98.75, 98.75, 101, 101, 100, 100, 99.94],
                        backgroundColor: '#26bcc2',
                        borderWidth: 0,
                        datalabels: {
                            align: 'end',
                            anchor: 'end',
                        },
                        barPercentage: 0.5,
                    },
                ],
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    height: 100vh;

    .main {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding-top: 90px;
        box-sizing: border-box;
        height: 100%;

        .statistics {
            display: flex;
            flex-direction: column;
            box-sizing: border-box;
            min-width: 350px;
            max-width: 370px;
            margin-left: 25px;
            background-color: #fff;
            height: 100%;
            min-height: 300px;
            flex: 1;
            &__main {
                margin-left: 20px;
                margin-top: 38px;
                display: flex;
                flex-direction: column;
                &__item {
                    display: flex;
                    flex-direction: row;
                    align-items: center;
                    padding-bottom: 10px;
                    .statistic-title {
                        width: 200px;
                        font-size: 24px;
                        color: #808080;
                    }
                    .statistic-result {
                        font-size: 24px;
                        color: #1a2740;
                        padding-left: 24px;
                        font-weight: bolder;
                    }
                    &:nth-of-type(3) {
                        padding-bottom: 20px;
                    }
                }
            }
            &__best {
                margin-top: 40px;
                margin-left: 20px;
                &__header {
                    margin-bottom: 20px;
                    .header-title {
                        font-size: 24px;
                        color: #1a2740;
                    }
                    .header-date {
                        font-size: 24px;
                        color: #808080;
                    }
                }
                &__item {
                    display: flex;
                    flex-direction: row;
                    align-items: center;
                    padding-bottom: 10px;
                    .best-title {
                        width: 200px;
                        font-size: 24px;
                        color: #808080;
                    }
                    .best-result {
                        font-size: 24px;
                        color: #1a2740;
                        padding-left: 15px;
                        font-weight: bolder;
                    }
                }
            }
        }

        .achievements {
            display: flex;
            flex-direction: column;
            height: 100%;
            overflow: auto;
            flex: 1;
            padding: 25px;
            box-sizing: border-box;
            &__title {
                font-size: 24px;
                color: #545969;
            }
            &__item {
                display: flex;
                margin-top: 30px;
                background-color: #fff;
                box-shadow: 0px 5px 5px -5px rgba(34, 60, 80, 0.69);
                min-width: 450px;
                width: 100%;
                padding: 8px;
                box-sizing: border-box;
                &__img-container {
                    flex-shrink: 0;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    margin-right: 8px;
                    position: relative;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;

                    .image {
                        border: none;
                        display: block;
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        position: absolute;
                        top: 0;
                        left: 0;
                    }
                }

                &:nth-of-type(odd) > .achievements__item__img-container {
                    background-color: #f7d9b9;
                }

                &:nth-of-type(even) > .achievements__item__img-container {
                    background-color: #23adb2;
                }

                &__content {
                    display: flex;
                    flex-direction: column;
                    flex: 1;
                    .achievement-title {
                        font-size: 18px;
                        color: #1a2740;
                        &:nth-of-type(1) {
                            padding-top: 9px;
                        }
                        &:nth-of-type(2) {
                            padding-top: 15px;
                        }
                    }
                    .achievement-description {
                        padding-top: 10px;
                        font-size: 16px;
                        color: #1a2740;
                    }
                    .achievement-date {
                        font-size: 16px;
                        color: #b1b2b7;
                        margin: 10px 0 10px auto;
                    }
                }
            }
        }

        .indicators {
            display: flex;
            flex-direction: column;
            height: 100%;
            overflow: auto;
            flex: 1.2;
            padding: 25px;
            box-sizing: border-box;
            &__title {
                font-size: 24px;
                color: #545969;
            }
            &__item {
                display: flex;
                flex-direction: column;
                background-color: #fff;
                margin-top: 30px;
                box-shadow: 0px 5px 5px -5px rgba(34, 60, 80, 0.69);
                width: 100%;
                padding: 8px;
                box-sizing: border-box;
            }
            &__wrap-graph {
                height: 110px;

                > div {
                    position: relative;
                    height: 100%;
                }
            }

            &__category {
                padding-bottom: 30px;
                color: #1a2740;
                font-size: 16px;
            }

            &__time-period {
                font-size: 16px;
                color: #b1b2b7;
                margin: 10px 0 10px auto;
            }
        }
    }
}
</style>
