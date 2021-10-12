<template>
    <div class="wrapper">
        <div class="test-container">
            <div v-if="getAnswersResult.status === 'notReady'" class="test">
                <Spinner
                    v-if="getQuestionsList.status === 'loading'"
                    class="loading"
                    :style="{ margin: 'auto', width: '50px' }"
                    :size="25"
                    :line-bg-color="'#b1b2b7'"
                    :line-fg-color="'#26bcc2'"
                />
                <span
                    v-else-if="getQuestionsList.status === 'error'"
                    :style="{ margin: 'auto', color: '#545969' }"
                    >Тест не найден</span
                >
                <template v-else-if="getQuestionsList.status === 'success'">
                    <div class="test-block">
                        <div class="test__progress">
                            <router-link class="progress-close" to="/tests"
                                ><Close
                            /></router-link>
                            <progress
                                class="progress-bar"
                                :value="openedQuestionInd + 1"
                                :max="getQuestionsList.data.questions.length"
                            ></progress>
                        </div>
                        <h2 class="test__name">
                            {{ getQuestionsList.data.testInfo.title }}
                        </h2>
                    </div>

                    <QuestionBlock
                        :question-number="openedQuestionInd + 1"
                        :question-info="
                            getQuestionsList.data.questions[openedQuestionInd]
                        "
                        :select-option="selectOption"
                        :choosed-answer="userAnswers[openedQuestionInd]"
                    />
                    <div class="test__nav-btns-container">
                        <button
                            v-if="openedQuestionInd !== 0"
                            class="nav-btn prev active"
                            @click="prevQuestion()"
                        >
                            Назад
                        </button>
                        <button
                            v-if="
                                openedQuestionInd <
                                    getQuestionsList.data.questions.length - 1
                            "
                            class="nav-btn active"
                            :disabled="
                                !userAnswers[openedQuestionInd] ||
                                    !userAnswers[openedQuestionInd].answer
                            "
                            @click="nextQuestion()"
                        >
                            Дальше
                        </button>

                        <button
                            v-else
                            class="nav-btn active"
                            :disabled="!isCompleted"
                            @click="endTest()"
                        >
                            Завершить тест
                        </button>
                    </div>
                </template>
            </div>
            <div v-else class="test-passed">
                <Spinner
                    v-if="getAnswersResult.status === 'loading'"
                    class="loading"
                    :style="{ margin: 'auto', width: '50px' }"
                    :size="25"
                    :line-bg-color="'#b1b2b7'"
                    :line-fg-color="'#26bcc2'"
                />
                <template v-if="getAnswersResult.status === 'success'">
                    <Medal
                        v-if="getAnswersResult.data.status === 'done'"
                        class="test-passed__medal"
                    />
                    <h2 class="test-passed__headline">
                        {{
                            getAnswersResult.data.status === 'done'
                                ? 'Тест пройден'
                                : 'Тест провален'
                        }}
                    </h2>
                    <div class="test-passed__statistic">
                        <div class="statistic__rights-answers">
                            <Complete class="rights-answers__icon" /> Правильных
                            {{ getAnswersResult.data.right_answers }} из
                            {{ getAnswersResult.data.total_questions }}
                        </div>
                        <!-- <div class="statistic__time">
                            <Time class="time__icon" />{{ leadTime }}
                        </div> -->
                    </div>
                    <div
                        v-if="getAnswersResult.data.status === 'done'"
                        class="test-passed__reward"
                    >
                        <div class="reward__coins">
                            <CoinSvg class="coins__icon" />{{
                                getAnswersResult.data.money
                            }}
                        </div>
                        <div class="reward__lightning">
                            <LightningSvg class="lightning__icon" />{{
                                getAnswersResult.data.energy
                            }}
                        </div>
                    </div>
                    <router-link class="test-passed__back" to="/tests"
                        >К списку тестов</router-link
                    >
                </template>
            </div>
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
// import Time from '@/assets/icons/tests/time.svg'
import QuestionBlock from '@/components/QuestionBlock.vue'
import {
    QUESTIONS_REQUEST,
    SEND_ANSWERS_REQUEST,
} from '@/store/action-types/tests'
import { PROFILE_UPDATE } from '@/store/action-types/profile'
import { mapGetters, mapActions } from 'vuex'
import Spinner from 'vue-simple-spinner'
export default {
    components: {
        Close,
        Medal,
        LightningSvg,
        CoinSvg,
        Complete,
        // Time,
        QuestionBlock,
        Spinner,
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
            openedQuestionInd: 0,
            selectedValue: null,
            currentQuestionNumber: 0,
            rightAnswers: 0,
            userAnswers: [],
            reward: {},
            isCompleted: false,
        }
    },

    computed: {
        ...mapGetters('tests', [
            'getTests',
            'getQuestionsList',
            'getAnswersResult',
        ]),
        test: function() {
            return this.getTests.filter(
                test => test.id === parseInt(this.id, 10)
            )[0]
        },
    },
    watch: {
        userAnswers: function(newVal) {
            console.log(newVal)
        },
    },
    async mounted() {
        await this.QUESTIONS_REQUEST(this.id)
        if (this.getQuestionsList.data !== null) {
            this.getQuestionsList.data.questions.forEach(question => {
                this.userAnswers.push({
                    question: question.question.id,
                    answerType: question.question.answerType,
                    answer: null,
                })
            })
        }
    },
    methods: {
        ...mapActions('tests', [QUESTIONS_REQUEST, SEND_ANSWERS_REQUEST]),
        ...mapActions('profile', [PROFILE_UPDATE]),
        checkIsCompleted: function() {
            return (
                this.userAnswers.filter(item => item.answer === null).length ===
                0
            )
        },
        selectOption: function(option) {
            switch (this.userAnswers[this.openedQuestionInd].answerType) {
                case 'one_choice':
                    if (
                        this.userAnswers[this.openedQuestionInd].answer ===
                        option
                    )
                        this.userAnswers[this.openedQuestionInd].answer = null
                    else
                        this.userAnswers[this.openedQuestionInd].answer = option
                    break
                case 'multi_choice':
                    if (
                        this.userAnswers[this.openedQuestionInd].answer === null
                    )
                        this.userAnswers[this.openedQuestionInd].answer = [
                            option,
                        ]
                    else {
                        if (
                            this.userAnswers[this.openedQuestionInd].answer
                                .length === 1 &&
                            this.userAnswers[this.openedQuestionInd]
                                .answer[0] === option
                        )
                            this.userAnswers[
                                this.openedQuestionInd
                            ].answer = null
                        else if (
                            this.userAnswers[
                                this.openedQuestionInd
                            ].answer.includes(option)
                        ) {
                            this.userAnswers[
                                this.openedQuestionInd
                            ].answer = this.userAnswers[
                                this.openedQuestionInd
                            ].answer.filter(answ => answ !== option)
                        } else
                            this.userAnswers[
                                this.openedQuestionInd
                            ].answer.push(option)
                    }
                    break
                case 'enter_text':
                case 'enter_number':
                    if (option === '')
                        this.userAnswers[this.openedQuestionInd].answer = null
                    else
                        this.userAnswers[this.openedQuestionInd].answer = option
                    break
                default:
                    break
            }
            this.isCompleted = this.checkIsCompleted()
        },
        nextQuestion: function() {
            this.openedQuestionInd += 1
        },
        prevQuestion: function() {
            this.openedQuestionInd -= 1
        },
        endTest: async function() {
            await this.SEND_ANSWERS_REQUEST({
                answers: this.userAnswers,
                testId: this.id,
            })
            await this.PROFILE_UPDATE()
        },
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    height: 100vh;
    display: flex;
    justify-content: center;
}
.test-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding-top: 140px;
    width: 70%;
    overflow-y: auto;
    .test {
        width: 100%;
        display: flex;
        flex-direction: column;
        background: #ffffff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        justify-content: flex-start;
        align-items: center;
        padding: 25px 150px;
        height: 70vh;
        .test-block {
            width: 100%;
            margin-bottom: 15px;
        }
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
            margin-top: 20px;
            font-size: 24px;
            color: #000;
            text-align: center;
        }
        &__nav-btns-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-top: auto;
            .nav-btn {
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
                justify-self: space-between;
                margin-bottom: 10px;
                &:disabled {
                    border: none;
                    outline: none;
                    background: #abb2c7;
                    color: #545969;
                    cursor: unset;
                }
                &:last-child {
                    margin-bottom: 0;
                }
            }
            .prev {
                background: transparent;

                &:disabled {
                    border: 2px solid #abb2c7;
                    outline: none;
                    background: transparent;
                    color: #545969;
                    cursor: unset;
                }
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
