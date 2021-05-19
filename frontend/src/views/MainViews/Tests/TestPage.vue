<template>
    <div class="tests-wrapper">
        <div v-if="testStatus" class="test">
            <div class="test__progress">
                <router-link class="progress-close" to="/tests"
                    ><Close
                /></router-link>
                <progress
                    class="progress-bar"
                    :value="currentQuestionNumber + 1"
                    :max="test.questions.length"
                ></progress>
            </div>
            <h2 class="test__name">{{ test.name }}</h2>
            <h3 class="test__question-number">
                Вопрос {{ currentQuestionNumber + 1 }}
            </h3>
            <p class="test__question-description">
                {{ test.questions[currentQuestionNumber].question }}
            </p>
            <div
                v-for="option in test.questions[currentQuestionNumber].options"
                :key="option"
                class="test__answer-options"
            >
                <button
                    class="answer-option"
                    :class="{ active: selectedValue == option }"
                    @click="selectOption(option)"
                >
                    {{ option }}
                </button>
            </div>
            <button
                v-if="currentQuestionNumber < test.questions.length - 1"
                class="test__next active"
                :disabled="!selectedValue"
                @click="nextQuestion()"
            >
                Дальше
            </button>
            <button
                v-else
                class="test__next active"
                :disabled="!selectedValue"
                @click="endTest()"
            >
                Завершить тест
            </button>
        </div>
        <div v-else class="test-passed">
            <Medal class="test-passed__medal" />
            <h2 class="test-passed__headline">Тест пройден</h2>
            <div class="test-passed__statistic">
                <div class="statistic__rights-answers">
                    <Complete class="rights-answers__icon" />{{
                        rightAnswers
                    }}
                    из {{ test.questions.length }}
                </div>
                <div class="statistic__time">
                    <Time class="time__icon" />{{ leadTime }}
                </div>
            </div>
            <div class="test-passed__reward">
                <div class="reward__coins">
                    <CoinSvg class="coins__icon" />{{ reward.coins }}
                </div>
                <div class="reward__lightning">
                    <LightningSvg class="lightning__icon" />{{
                        reward.lightnings
                    }}
                </div>
            </div>
            <router-link class="test-passed__back" to="/tests"
                >К списку тестов</router-link
            >
        </div>
    </div>
</template>

<script>
// icons
import Close from '@/assets/icons/tests/close.svg'
import Medal from '@/assets/icons/tests/medal.svg'
import LightningSvg from '@/assets/icons/lightning.svg'
import CoinSvg from '@/assets/icons/coin.svg'
import Complete from '@/assets/icons/tests/complete.svg'
import Time from '@/assets/icons/tests/time.svg'

import { mapGetters } from 'vuex'
import { mapMutations } from 'vuex'
export default {
    components: {
        Close,
        Medal,
        LightningSvg,
        CoinSvg,
        Complete,
        Time,
    },
    props: {
        id: {
            default: '0',
            type: String,
        },
    },
    data() {
        return {
            testStatus: true,
            startTime: new Date(),
            leadTime: '',
            selectedValue: null,
            currentQuestionNumber: 0,
            rightAnswers: 0,
            reward: {},
        }
    },
    computed: {
        ...mapGetters('tests', ['getTests']),
        test: function() {
            return this.getTests.filter(
                test => test.id === parseInt(this.id, 10)
            )[0]
        },
        // numberQuestions: function() {
        //     return this.test.questions.length
        // },
    },
    methods: {
        ...mapMutations(['accrueReward']),
        selectOption: function(option) {
            if (this.selectedValue === option) {
                this.selectedValue = null
            } else {
                this.selectedValue = option
            }
        },
        nextQuestion: function() {
            if (
                this.test.questions[this.currentQuestionNumber].answer ===
                this.selectedValue
            ) {
                this.rightAnswers += 1
            }
            this.currentQuestionNumber += 1
            this.selectedValue = null
        },
        endTest: function() {
            if (
                this.test.questions[this.currentQuestionNumber].answer ===
                this.selectedValue
            ) {
                this.rightAnswers += 1
            }
            this.testStatus = false
            let endTime = new Date()
            let ms = endTime - this.startTime
            let toDate = new Date(ms)
            this.leadTime =
                toDate.getUTCMinutes() + ':' + toDate.getUTCSeconds()
            let coins = Math.round(
                this.test.reward.coins *
                    (this.rightAnswers / this.test.questions.length)
            )
            let lightnings = Math.round(
                this.test.reward.lightnings *
                    (this.rightAnswers / this.test.questions.length)
            )
            this.reward = {
                coins: coins,
                lightnings: lightnings,
            }
            this.$store.commit('accrueReward', this.reward)
            this.$store.commit('tests/deleteTest', this.test.id)
        },
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.tests-wrapper {
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 90px;
    height: calc(100vh - 90px);
    width: 100%;
    overflow-y: auto;
    .test {
        display: flex;
        flex-direction: column;
        background: #ffffff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        justify-content: space-between;
        align-items: center;
        padding: 24px 154px 50px 154px;
        margin-top: 68px;
        width: 975px;
        height: 663px;
        &__progress {
            display: flex;
            flex-direction: row;
            justify-content: center;
            width: 100%;
            .progress {
                &-close {
                    width: 23.35px;
                    height: 19px;
                    background: transparent;
                    border: none;
                    outline: none;
                    cursor: pointer;
                    margin-right: 6px;
                }
                &-bar {
                    height: 17px;
                    display: block;
                    appearance: none;
                    -webkit-appearance: none;
                    border-radius: 10px;
                    width: 100%;
                    &::-webkit-progress-bar {
                        background-color: #d8dcea;
                        border-radius: 10px;
                    }
                    &::-webkit-progress-value {
                        background: #26bcc2;
                        border-radius: 10px;
                    }
                }
            }
        }
        &__name {
            font-size: 24px;
            line-height: 33px;
            color: #000;
        }
        &__question-number {
            font-size: 24px;
            line-height: 33px;
            color: #545969;
        }
        &__question-description {
            font-size: 18px;
            line-height: 25px;
            text-align: center;
            color: #1a2740;
            width: 425px;
            margin-bottom: 46px;
        }
        &__answer-options {
            display: flex;
            flex-direction: column;
            .answer-option {
                &.active {
                    background: #fff;
                    border: 2px solid #26bcc2;
                    border-bottom: 4px solid #26bcc2;
                }
                background: #d8dcea;
                border: 2px solid #abb2c7;
                border-bottom: 4px solid #abb2c7;
                box-sizing: border-box;
                border-radius: 10px;
                outline: none;
                margin-bottom: 21px;
                font-size: 14px;
                line-height: 19px;
                color: #1a2740;
                width: 312px;
                height: 41px;
                cursor: pointer;
                &:last-child {
                    margin-bottom: 0;
                }
            }
        }
        &__next {
            box-sizing: border-box;
            background: #89dce0;
            border-radius: 10px;
            border: none;
            border: 2px solid #26bcc2;
            border-bottom: 4px solid #26bcc2;
            outline: none;
            font-size: 14px;
            line-height: 19px;
            color: #1a2740;
            width: 312px;
            height: 41px;
            cursor: pointer;
            &:disabled {
                border: none;
                outline: none;
                background: #abb2c7;
                color: #545969;
                cursor: unset;
            }
        }
    }
    .test-passed {
        margin-top: 118px;
        display: flex;
        flex-direction: column;
        align-items: center;
        &__medal {
            width: 151px;
            height: 151px;
        }
        &__headline {
            margin-top: 14px;
            margin-bottom: 37px;
            font-size: 24px;
            line-height: 33px;
            color: #545969;
        }
        &__statistic {
            display: flex;
            flex-direction: row;
            font-size: 18px;
            line-height: 25px;
            color: #545969;
            margin-bottom: 27px;
            .statistic {
                &__rights-answers {
                    display: flex;
                    align-items: center;
                    .rights-answers__icon {
                        width: 24px;
                        height: 24px;
                    }
                }
                &__time {
                    display: flex;
                    align-items: center;
                    margin-left: 23px;
                    .time__icon {
                        width: 21.64px;
                        height: 24.59;
                    }
                }
            }
        }
        &__reward {
            display: flex;
            flex-direction: row;
            font-size: 18px;
            line-height: 16px;
            .reward__coins {
                display: flex;
                align-items: center;
                color: #f2af49;
                .coins__icon {
                    height: 24px;
                    width: 24px;
                }
            }
            .reward__lightning {
                display: flex;
                align-items: center;
                color: #50af8d;
                margin-left: 23px;
                .lightning__icon {
                    width: 14.62px;
                    height: 24px;
                }
            }
        }
        &__back {
            display: flex;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
            background: #89dce0;
            border-radius: 10px;
            border: none;
            border: 2px solid #26bcc2;
            border-bottom: 4px solid #26bcc2;
            outline: none;
            font-size: 14px;
            line-height: 19px;
            color: #1a2740;
            width: 312px;
            height: 41px;
            margin-top: 85px;
            cursor: pointer;
            text-decoration: none;
        }
    }
}
</style>
