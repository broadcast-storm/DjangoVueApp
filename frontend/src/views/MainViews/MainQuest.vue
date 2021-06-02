<template>
    <div class="wrapper">
        <div class="main">
            <div class="mainQuestInfo-wrap">
                <template
                    v-if="
                        mainQuest.status === 'success' &&
                            !(
                                mainQuest.data === null ||
                                mainQuest.data.length === 0
                            )
                    "
                >
                    <div class="text__gray__big">Основной квест:</div>
                    <h1 class="test-headline">{{ mainQuest.data[0].title }}</h1>
                    <ProgressBar
                        :percent="
                            mainQuest.data[0].progress === undefined
                                ? 0
                                : mainQuest.data[0].progress
                        "
                        class="progress-bar"
                    />
                    <div class="text_deadline">
                        <div class="text__gray">Срок:</div>
                        <div class="date">
                            до 6.06.2021 {{ mainQuest.data[0].deadline }}
                        </div>
                    </div>
                    <div class="tasks">
                        <h2 class="tasks__title">Список задач</h2>
                        <div class="tasks__list">
                            <Task
                                v-for="subTask in mainQuest.data[0].subTasks"
                                :key="subTask.id"
                                :data="subTask"
                                class="tasks__item"
                            />
                        </div>
                    </div>
                </template>
                <div
                    v-if="
                        mainQuest.status === 'loading' ||
                            (mainQuest.status === 'success' &&
                                (mainQuest.data === null ||
                                    mainQuest.data.length === 0))
                    "
                    :style="{
                        height: '100%',
                        display: 'flex',
                        justifyContent: 'center',
                        alignItems: 'center',
                    }"
                >
                    <Spinner
                        v-if="mainQuest.status === 'loading'"
                        :size="25"
                        :line-bg-color="'#b1b2b7'"
                        :line-fg-color="'#26bcc2'"
                    />
                    <span
                        v-if="
                            mainQuest.status === 'success' &&
                                (mainQuest.data === null ||
                                    mainQuest.data.length === 0)
                        "
                        style="color:#1a2740"
                        >Нет активного основного квеста</span
                    >
                </div>
            </div>
            <div class="tree_wrap">
                <span>Здесь будет граф основного квеста</span>
            </div>
        </div>
    </div>
</template>

<script>
import Task from '@/components/Task.vue'
import ProgressBar from '@/components/ProgressBar.vue'
import { mapGetters, mapActions } from 'vuex'
import { MAIN_QUEST_REQUEST } from '@/store/action-types/tasks'
import Spinner from 'vue-simple-spinner'

export default {
    name: 'MainQuest',
    components: {
        Task,
        ProgressBar,
        Spinner,
    },
    computed: {
        ...mapGetters('tasks', ['mainQuest']),
    },
    async mounted() {
        if (this.mainQuest.status !== 'success') await this.MAIN_QUEST_REQUEST()
    },
    methods: {
        ...mapActions('tasks', [MAIN_QUEST_REQUEST]),
    },
}
</script>

<style lang="scss" scoped>
.wrapper {
    height: 100vh;
}
.main {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    box-sizing: border-box;
    padding-top: 150px;
    height: 100%;
    width: 100%;
}
.mainQuestInfo-wrap {
    min-width: 450px;
    max-width: 550px;
    width: 40%;
    height: 75vh;
    border: 1px solid #b1b2b7;
    box-sizing: border-box;
    margin: 0 20px 0 20px;
    padding: 30px 30px 0 30px;
}

.tasks {
    box-sizing: border-box;
    &__list {
        height: 38vh;
        overflow-y: auto;
        min-height: 290px;
    }
    &__title {
        font-size: 24px;
        font-weight: 400;
        color: #1a2740;
        margin-bottom: 20px;
    }

    &__item:not(:first-child) {
        margin-top: 30px;
    }
}

.text_deadline {
    margin-bottom: 30px;
}

.date {
    display: inline-block;
    margin-left: 5px;
    font-size: 18px;
}

.text {
    &__gray {
        display: inline-block;
        color: #545969;
        font-size: 18px;
        line-height: 16px;
        &__big {
            color: #545969;
            font-size: 24px;
            line-height: 16px;
        }
    }
}
.test-headline {
    margin-top: 10px;
    font-size: 36px;
}
.progress-bar {
    max-width: 407px;
    margin-top: 23px;
    margin-bottom: 10px;
}
.progressbar {
    background-color: #fff;
    margin-top: 10px;
}

.tree_wrap {
    border: 1px solid #b1b2b7;
    box-sizing: border-box;
    min-width: 450px;
    max-width: 550px;
    height: 75vh;
    width: 40%;
    background-color: white;
    margin: 0 20px 0 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #1a2740;
}
</style>
