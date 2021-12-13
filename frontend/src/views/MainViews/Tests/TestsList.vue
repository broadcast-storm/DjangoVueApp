<template>
    <div class="wrapper">
        <div class="tests-container">
            <h2 class="tests__headline">
                Доступные тесты
            </h2>
            <div
                v-if="
                    getTestsList.status === 'success' &&
                        getTestsList.data.length !== 0
                "
                class="tests__list"
            >
                <Test
                    v-for="test in getTestsList.data"
                    :key="test.id"
                    :test-info="test"
                />
            </div>
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
    </div>
</template>

<script>
import Test from '@/components/Test.vue'
import { mapGetters, mapActions } from 'vuex'
import { TESTS_REQUEST } from '@/store/action-types/tests'
import Spinner from 'vue-simple-spinner'

export default {
    components: {
        Spinner,
        Test,
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
            return '/tests/' + itemId
        },
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    min-height: 100vh;
}
.tests-container {
    padding: 140px 0 0 60px;
    height: 100%;
    width: 460px;

    .tests {
        &__headline {
            font-size: 24px;
            color: #545969;
        }
        &__list {
            margin-top: 20px;
            padding-bottom: 10px;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            height: 75vh;
            overflow-y: auto;
            min-height: 290px;
            overflow-y: auto;
        }
    }
}
</style>
