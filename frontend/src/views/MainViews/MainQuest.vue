<template>
    <div>
        <div class="mainQuest-wrap">
            <div class="mainQuestInfo-wrap">
                <div class="text__gray__big">Основной квест:</div>
                <h1 class="test-headline">{{ mainQuest.taskname }}</h1>
                <ProgressBar
                    :percent="mainQuest.progress"
                    class="progress-bar"
                />
                <div class="text_deadline">
                    <div class="text__gray">Срок:</div>
                    <div class="date">до {{ mainQuest.deadline }}</div>
                </div>
                <div class="tasks" :style="{ height: commonHeight }">
                    <h2 class="tasks__title">Список задач</h2>
                    <Task
                        v-for="subtask in mainQuest.subtasks"
                        :key="subtask.id"
                        :data="subtask"
                        class="tasks__item"
                    />
                </div>
            </div>
            <div class="tree_wrap"></div>
        </div>
    </div>
</template>

<script>
import Task from '@/components/Task.vue'
import ProgressBar from '@/components/ProgressBar.vue'
export default {
    name: 'MainQuest',
    components: {
        Task,
        ProgressBar,
    },
    data() {
        return {
            mainQuest: Object.assign({}, this.$store.getters.getMainQuest),
            tasks: Object.assign({}, this.$store.getters.getTasks),
        }
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.mainQuest-wrap {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    margin-top: 90px;
    height: calc(100vh - 90px);
    width: 100%;
    overflow-y: auto;
}
.mainQuestInfo-wrap {
    display: inline;
    position: relative;
    max-width: 470px;
    min-height: 793px;
    max-height: 793px;
    border: 1px solid #b1b2b7;
    box-sizing: border-box;
    margin: 59px 45px 91px 18px;
}

.tasks {
    box-sizing: border-box;
    min-height: 470px;
    max-height: 540px;
    width: 400px;
    overflow-y: auto;
    min-width: 412px;
    margin-left: 33px;
    margin-right: 30px;

    &__title {
        font-size: 24px;
        font-weight: 400;
        line-height: 16px;
        color: #1a2740;
        margin-top: 1px;
        margin-bottom: 35px;
    }

    &__item:not(:first-child) {
        margin-top: 30px;
    }
}

.date {
    display: inline-block;
    margin-left: 5px;
    margin-bottom: 58px;
    font-size: 18px;
}

.text {
    &__gray {
        display: inline-block;
        margin-left: 33px;
        color: #545969;
        font-size: 18px;
        line-height: 16px;
        &__big {
            margin-left: 33px;
            color: #545969;
            margin-top: 36px;
            font-size: 24px;
            line-height: 16px;
        }
    }
}
.test-headline {
    margin-top: 19px;
    margin-left: 33px;
    font-size: 36px;
    line-height: 16px;
}
.progress-bar {
    max-width: 407px;
    margin-top: 23px;
    margin-left: 33px;
    margin-right: 30px;
    margin-bottom: 10px;
}
.progressbar {
    background-color: #fff;
}

.tree_wrap {
    display: inline;
    border: 1px solid #b1b2b7;
    box-sizing: border-box;
    width: 568px;
    height: 793px;
    background-color: white;
    margin: 59px 45px 91px 0;
}
</style>
