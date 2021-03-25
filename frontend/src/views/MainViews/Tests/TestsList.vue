<template>
    <div class="tests-wrapper">
        <h2 class="tests__headline">
            Доступные тесты
        </h2>
        <div class="tests__list" v-for="test in tests" :key="test.id">
            <div class="test">
                <h3 class="test-headline">
                    {{ test.name }}
                </h3>
                <div class="test-wrap">
                    <span class="test-description">{{ test.description }}</span
                    ><router-link class="test-begin" :to="getLink(test.id)">
                        Начать<Arrow class="arrow" />
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Arrow from '@/assets/icons/arrow-rigth.svg'
import { mapGetters } from 'vuex'
export default {
    components: {
        Arrow,
    },
    data() {
        return {}
    },
    computed: {
        ...mapGetters('tests', ['getTests']),
        tests: function() {
            return this.getTests
        },
    },
    methods: {
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
