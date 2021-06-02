<template>
    <div class="tests-wrapper">
        <h2 class="tests__headline">
            Доступные тесты
        </h2>
        <template
            v-if="
                getTestsList.status === 'success' &&
                    getTestsList.data.length !== 0
            "
        >
            <div
                v-for="test in getTestsList.data"
                :key="test.id"
                class="tests__list"
            >
                <div v-if="test.status !== 'Passed'" class="test">
                    <h3 class="test-headline">
                        {{ test.title }}
                    </h3>
                    <div class="test-wrap">
                        <span class="test-description">{{
                            test.description
                        }}</span
                        ><router-link class="test-begin" :to="getLink(test.id)">
                            Начать<Arrow class="arrow" />
                        </router-link>
                    </div>
                </div>
            </div>
        </template>
        <span
            v-if="
                getTestsList.status === 'success' &&
                    getTestsList.data.length === 0
            "
            class="tests__list"
            >Нет доступных тестов</span
        >
        <Spinner
            v-if="getTestsList.status === 'loading'"
            class="tests__list"
            :style="{ marginTop: '50px', width: '50px' }"
            :size="25"
            :line-bg-color="'#b1b2b7'"
            :line-fg-color="'#26bcc2'"
        />
    </div>
</template>

<script>
import Arrow from '@/assets/icons/arrow-rigth.svg'
import { mapGetters, mapActions } from 'vuex'
import { TESTS_REQUEST } from '@/store/action-types/tests'
import Spinner from 'vue-simple-spinner'

export default {
    components: {
        Arrow,
        Spinner,
    },
    data() {
        return {}
    },
    computed: {
        ...mapGetters('tests', ['getTests', 'getTestsList']),
        tests: function() {
            return this.getTests
        },
    },
    async mounted() {
        await this.TESTS_REQUEST()
        console.log(this.getTestsList)
    },
    methods: {
        ...mapActions('tests', [TESTS_REQUEST]),
        getLink: function(itemId) {
            return '/tests/test/' + itemId
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
    flex-direction: column;
    justify-content: flex-start;
    margin-top: 90px;
    height: calc(100vh - 90px);
    width: 100%;
    overflow-y: auto;
    .tests {
        &__headline {
            font-style: normal;
            font-weight: normal;
            font-size: 24px;
            line-height: 33px;
            color: #545969;
            margin-top: 30px;
            margin-left: 67px;
        }
        &__list {
            display: flex;
            flex-direction: column;
            margin-top: 21px;
            margin-left: 67px;
            .test {
                background: #ffffff;
                box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                width: 456px;
                margin-bottom: 17px;
                padding: 13px 15.46px 16.86px 15.46px;
                &-headline {
                    font-size: 18px;
                    line-height: 16px;
                    color: #1a2740;
                }
                &-wrap {
                    display: flex;
                    flex-direction: row;
                    justify-content: space-between;
                    .test-description {
                        font-size: 14px;
                        line-height: 15px;
                        color: #7d849a;
                        margin-top: 3px;
                        margin-right: 25.3px;
                    }
                    .test-begin {
                        background: #26bcc2;
                        border-radius: 5px;
                        font-size: 14px;
                        line-height: 19px;
                        color: #fff;
                        border: none;
                        outline: none;
                        height: 22.48px;
                        padding-left: 13.76px;
                        padding-right: 10px;
                        min-width: 95.54px;
                        max-width: 95.54px;
                        // text-align: left;
                        align-self: flex-end;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        text-decoration: none;
                        cursor: pointer;
                        .arrow {
                            width: 9.33px;
                            height: 19px;
                        }
                    }
                }
            }
        }
    }
}
</style>
