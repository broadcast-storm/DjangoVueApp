<template>
    <div class="question">
        <h3 class="question__number">Вопрос {{ questionNumber }}</h3>
        <p class="question__description">
            {{ questionInfo.question.title }}
        </p>
        <div
            v-if="
                questionInfo.question.answerType === 'one_choice' ||
                    questionInfo.question.answerType === 'multi_choice'
            "
            class="question__answer-options"
        >
            <button
                v-for="option in questionInfo.answerOptions"
                :key="option.id"
                class="answer-option"
                :class="{ active: selectedValue == option.id }"
                @click="chooseOption(option.id)"
            >
                {{ option.text }}
            </button>
        </div>
        <div v-else class="question__input">
            <input
                v-if="questionInfo.question.answerType === 'enter_number'"
                type="number"
                class="input"
                placeholder="Введите число"
            />
            <input
                v-else-if="questionInfo.question.answerType === 'enter_text'"
                type="text"
                class="input"
                placeholder="Введите текст"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: 'QuestionBlock',
    props: {
        questionInfo: {
            type: Object,
            default: () => {},
        },
        questionNumber: {
            type: Number,
            default: 0,
        },
        selectOption: {
            type: Function,
            default: () => {},
        },
    },
    data() {
        return {
            selectedValue: null,
        }
    },
    methods: {
        chooseOption: function(option) {
            this.selectedValue = option
            this.selectOption(option)
        },
    },
}
</script>

<style lang="scss" scoped>
.question {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    &__number {
        font-size: 24px;
        color: #545969;
        text-align: center;
        margin-bottom: 16px;
    }
    &__description {
        font-size: 18px;
        line-height: 25px;
        text-align: center;
        color: #1a2740;
        width: 80%;
        margin-bottom: 40px;
    }
    &__answer-options {
        display: flex;
        flex-direction: column;
        align-items: center;
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
            margin-bottom: 20px;
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
    &__input {
        .input {
            background: #fff;
            border: 2px solid #abb2c7;
            border-bottom: 4px solid #abb2c7;
            box-sizing: border-box;
            border-radius: 10px;
            padding: 0 10px;
            outline: none;
            margin-bottom: 20px;
            font-size: 14px;
            line-height: 19px;
            color: #1a2740;
            width: 312px;
            height: 41px;
        }
    }
}
</style>
