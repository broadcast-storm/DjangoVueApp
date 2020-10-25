<template>
    <div class="task">
        <h4 class="task__name">{{ data.taskname }}</h4>
        <progressBar class="progressbar" :percent='data.progress' />
        <div class="task__info">
            <p class="task__type">тип: {{ data.type }}</p>
            <p class="task__deadline">
                <span v-if="showMore">Дэдлайн: </span>
                <span v-else>До: </span>
                {{ data.deadline }}
                </p>
            <div class="task__awards">
                <span v-show="showMore">Награда:</span>
                <div class="task__awards-content">
                    <div class="task__awards-content-item">
                        <CoinSvg class="task__awards-icon" />
                        {{ data.reward.coins }}
                    </div>
                    <div class="task__awards-content-item">
                        <LightningSvg class="task__awards-icon" />
                        {{ data.reward.lightnings }}
                    </div>
                </div>
            </div>
            <p v-show="showMore" class="task__difficulty">Сложность: {{ data.difficulty }}</p>
            <ol v-show="showMore" class="task__subtasks">
                <h6 class="task__subtasks-title">Подзадачи</h6>
                <li v-for="subtask in data.subtasks" :key="subtask.id"
                :style="[subtask.status == 'done' ? {'text-decoration': 'line-through'} : {'text-decoration': 'none'}]">
                    {{subtask.id}}. {{ subtask.title }}
                </li>
            </ol>
            <div v-show="showMore" class="task__desc">
                <h6 class="task__desc-title">Описание</h6>
                <p class="task__desc-text">{{ data.desc }}</p>
            </div>
        </div>
        <input v-model="showMore" class="task__toggle-inp" type="checkbox" :id="'task__toggle' + data.id">
        <label class="task__toggle" :for="'task__toggle' + data.id">
            <div class="arrow"></div>
            <div class="dot"></div>
        </label>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import LightningSvg from '@/assets/icons/lightning.svg'
import ProgressBar from '@/components/ProgressBar.vue'

export default {
    name: 'Task',
    components: {
        ProgressBar,
        CoinSvg,
        LightningSvg
    },
    props: {
        data: Object,
    },
    data() {
        return {
            showMore: false
        }
    }
}
</script>

<style lang="scss" scoped>

.task {
    width: 411px;
    max-width: 411px;
    background-color: $basic-white;
    box-sizing: border-box;
    padding: 6px 12px 13px 8px;
    font-size: 10px;
    line-height: 16px;
    font-weight: 400;
    color: $brand-night;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    position: relative;

    &__info {
        margin-top: 5px;
        display: grid;
        grid-template-columns: 1fr 1fr;
    }

    &__name {
        font-size: 16px;
        margin: 0;
        padding: 0;
    }

    &__subtasks {
        margin: 0;
        padding: 0;
        list-style: none;
        margin-top: 8px;
    }
    
    &__desc {
        margin-top: 8px;
    }

    &__subtasks-title,
    &__desc-title {
        font-size: 18px;
        margin-bottom: 5px;
    }


    &__desc-text {
        max-width: 163px;
    }

    /* Toggle menu button styles */

    &__toggle-inp {
        display: none;
    }

    &__toggle-inp:checked + &__toggle {

        flex-direction: column;
        align-items: center;

        .dot,
        .arrow {
            width: 0;
            display: block;
            height: 0;
            border: solid black;
            border-width: 0 2px 2px 0;
            padding: 3px;
            border-radius: 0;
            transform: rotate(-135deg);
            background-color: transparent;
        }

        .dot {
            margin-top: -2px;
        }

        .dot::after,
        .dot::before {
            display: none;
        }

    }

    &__toggle:hover {
        cursor: pointer;
    }

    &__toggle {
        box-sizing: border-box;
        display: block;
        width: 16px;
        display: flex;
        justify-content: center;
        position: absolute;
        top: 10px;
        right: 10px;
        padding: 2px;

        .arrow {
            display: none;
        }

        .dot,
        .dot::before,
        .dot::after {
            height: 4px;
            width: 4px;
            background-color: #000;
            border-radius: 50%;
        }

        .dot::before,
        .dot::after {
            content: '';
            position: absolute;
        }

        .dot::before {
            left: 0;
        }

        .dot::after {
            right: 0;
        }
    }
}

.task__awards {
    margin-top: 5px;
    display: flex;
    align-items: center;

    span {
        margin-right: 5px;
    }

    &-icon {
        width: 16px;
        height: 16px;
        margin-right: 2px;
    }

    &-content {
        width: 100px;
        display: flex;
        justify-content: space-between;
        align-items: center;

        &-item {
            display: flex;
            align-items: center;
        }
    }
}

.progressbar {
    color: #fff;
    width: 386px;
    margin-top: 13px;
}
</style>