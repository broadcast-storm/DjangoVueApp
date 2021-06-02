<template>
    <div>
        <div v-if="profileStatus === 'success'" class="profile-wrapper">
            <div class="column-wrap wrap__profile">
                <div ref="profile" class="profile">
                    <div class="profile__main-info">
                        <div class="profile__main-info__photo">
                            <img
                                :src="profileInfo.photo"
                                alt="User photo"
                                class="img"
                            />
                        </div>
                        <div class="profile__main-info__text">
                            <h2 class="text__name">
                                {{
                                    profileInfo.surname + ' ' + profileInfo.name
                                }}
                                <span class="text__name__patronymic">
                                    {{ profileInfo.patronymic }}
                                </span>
                            </h2>
                            <p class="text__department">
                                {{ profileInfo.division_details.title }}
                            </p>
                            <p class="text__bio">
                                {{ profileInfo.description }}
                            </p>
                            <p class="text__level">
                                Текущий уровень
                                <span class="text__level__count">
                                    {{ profileInfo.level }}
                                </span>
                            </p>
                        </div>
                    </div>

                    <div class="profile__stats">
                        <div class="profile__stats-item">
                            <CoinSvg class="profile__stats-icon" />
                            <span class="profile__stats-value coins">{{
                                profileInfo.money
                            }}</span>
                        </div>
                        <div class="profile__stats-item">
                            <LightningSvg class="profile__stats-icon" />
                            <span class="profile__stats-value lightnings">{{
                                profileInfo.energy
                            }}</span>
                        </div>
                        <div class="profile__stats-item">
                            <HeartSvg class="profile__stats-icon" />
                            <span class="profile__stats-value hearts">{{
                                profileInfo.health
                            }}</span>
                        </div>
                    </div>
                    <div class="task-props">
                        <div class="profile__task">
                            <p class="profile__task-title">Основной квест:</p>
                            <template v-if="mainQuest.status === 'success'">
                                <h3 class="profile__task-name">
                                    {{ mainQuest.data[0].title }}
                                </h3>
                                <ProgressBar
                                    :percent="
                                        mainQuest.data[0].progress === undefined
                                            ? 0
                                            : mainQuest.data[0].progress
                                    "
                                    class="progress-bar"
                                />
                                <p class="profile__task-deadline">
                                    <span class="progress">
                                        <span class="gray-txt">Прогресс:</span
                                        >{{
                                            mainQuest.data[0].progress ===
                                            undefined
                                                ? 0
                                                : mainQuest.data[0].progress
                                        }}%
                                    </span>
                                    <span class="gray-txt">Срок:</span> до
                                    {{ date }}
                                </p>
                            </template>
                            <Spinner
                                v-if="mainQuest.status === 'loading'"
                                :size="25"
                                :line-bg-color="'#b1b2b7'"
                                :line-fg-color="'#26bcc2'"
                            />
                        </div>
                        <table class="profile__props">
                            <tr class="profile__props-row">
                                <td class="profile__props-row-title">
                                    Продуктивность:
                                </td>
                                <td class="profile__props-row-value">
                                    {{ profileInfo.productivity }}%
                                </td>
                                <td class="profile__props-row-light">
                                    из 100% на сегодня
                                </td>
                            </tr>
                            <tr class="profile__props-row">
                                <td class="profile__props-row-title">
                                    Качество:
                                </td>
                                <td class="profile__props-row-value">
                                    {{ profileInfo.quality }}
                                </td>
                                <td class="profile__props-row-light">
                                    из 100 на сегодня
                                </td>
                            </tr>
                            <tr class="profile__props-row level">
                                <td class="profile__props-row-title">
                                    Текущий уровень:
                                </td>
                                <td class="profile__props-row-value">
                                    {{ profileInfo.level }}
                                </td>
                                <td></td>
                            </tr>
                        </table>
                    </div>
                </div>
            </div>
            <div class="profile-mobile-nav">
                <button
                    class="profile-mobile-nav__btn left-btn"
                    :class="{
                        active: screenMobile === 'tasks',
                    }"
                    @click="changeScreenMobile('tasks')"
                >
                    Задачи
                </button>
                <button
                    class="profile-mobile-nav__btn right-btn"
                    :class="{
                        active: screenMobile === 'achieves',
                    }"
                    @click="changeScreenMobile('achieves')"
                >
                    Достижения
                </button>
            </div>
            <div
                class="column-wrap wrap__tasks"
                :class="{
                    hide: screenMobile !== 'all' && screenMobile !== 'tasks',
                }"
            >
                <div class="tasks" :style="{ height: commonHeight }">
                    <h2 class="tasks__title">Список задач</h2>
                    <template
                        v-if="
                            dailyTasks.status === 'success' &&
                                weeklyTasks.status === 'success'
                        "
                    >
                        <span
                            v-if="
                                dailyTasks.status === 'success' &&
                                    weeklyTasks.status === 'success' &&
                                    dailyTasks.data === 0 &&
                                    weeklyTasks.data === 0
                            "
                            :style="{
                                display: 'inline-block',
                                width: '100%',
                                color: '#7d849a',
                                textAlign: 'center',
                                marginTop: '200px',
                            }"
                            >Нет активных задач</span
                        >
                        <template v-else>
                            <Task
                                v-for="task in tasksList"
                                :key="getTaskId(task.taskType, task.id)"
                                :data="task"
                                :custom-id="getTaskId(task.taskType, task.id)"
                                class="tasks__item"
                            />
                        </template>
                    </template>
                    <Spinner
                        v-if="
                            dailyTasks.status === 'loading' ||
                                weeklyTasks.status === 'loading'
                        "
                        :style="{ marginTop: '200px' }"
                        :size="25"
                        :line-bg-color="'#b1b2b7'"
                        :line-fg-color="'#26bcc2'"
                    />
                </div>
            </div>
            <div
                class="column-wrap wrap__achieves"
                :class="{
                    hide: screenMobile !== 'all' && screenMobile !== 'achieves',
                }"
            >
                <div class="achievements" :style="{ height: commonHeight }">
                    <h2 class="achievements__title">Ачивки</h2>
                    <div class="achievements__inner">
                        <div
                            v-for="achievement in user.achievements"
                            :key="achievement.id"
                            class="achievements__inner-item"
                        >
                            <img
                                class="achievements__inner-item__image"
                                alt=""
                                :src="
                                    achievement.status !== 'completed'
                                        ? 'https://via.placeholder.com/150/f7d9b9'
                                        : achievement.img
                                "
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import HeartSvg from '@/assets/icons/heart.svg'
import LightningSvg from '@/assets/icons/lightning.svg'
import ProgressBar from '@/components/ProgressBar.vue'
import Task from '@/components/Task.vue'
import { mapGetters, mapActions } from 'vuex'
import {
    WEEKLY_TASKS_REQUEST,
    DAILY_TASKS_REQUEST,
    MAIN_QUEST_REQUEST,
} from '@/store/action-types/tasks'
import Spinner from 'vue-simple-spinner'

export default {
    name: 'Profile',
    components: {
        CoinSvg,
        HeartSvg,
        LightningSvg,
        ProgressBar,
        Task,
        Spinner,
    },
    data() {
        return {
            commonHeight: '',
            windowWidth: window.innerWidth,
            screenMobile: window.innerWidth > 768 ? 'all' : 'tasks',
            user: Object.assign({}, this.$store.getters.getUserData),
            tasksList: [],
        }
    },
    computed: {
        ...mapGetters(['getUserData']),
        ...mapGetters('profile', ['profileStatus', 'profileInfo']),
        ...mapGetters('tasks', ['dailyTasks', 'weeklyTasks', 'mainQuest']),
        date() {
            const date = this.getUserData.task.deadline

            let month = date.getMonth() + 1
            let days = date.getDate()
            month = month < 10 ? '0' + month : month
            days = days < 10 ? '0' + days : days

            return days + '.' + month + '.' + date.getFullYear()
        },
    },
    watch: {
        windowWidth(newWidth) {
            if (newWidth > 768 && this.screenMobile !== 'all') {
                this.matchHeight()
                this.screenMobile = 'all'
            }
            if (newWidth < 768 && this.screenMobile === 'all') {
                this.commonHeight = 'auto'
                this.screenMobile = 'tasks'
            }
        },
    },
    async mounted() {
        this.$nextTick(() => {
            window.addEventListener('resize', this.onResize)
        })
        await this.WEEKLY_TASKS_REQUEST()
        await this.DAILY_TASKS_REQUEST()
        await this.MAIN_QUEST_REQUEST()
        if (
            this.dailyTasks.status === 'success' &&
            this.weeklyTasks.status === 'success'
        )
            this.weeklyTasks.data === null
                ? (this.tasksList = this.dailyTasks.data)
                : (this.tasksList = this.dailyTasks.data.concat(
                      this.weeklyTasks.data
                  ))
    },

    beforeDestroy() {
        window.removeEventListener('resize', this.onResize)
    },
    methods: {
        ...mapActions('tasks', [
            WEEKLY_TASKS_REQUEST,
            DAILY_TASKS_REQUEST,
            MAIN_QUEST_REQUEST,
        ]),
        getTaskId: function(type, id) {
            return type === 'quest'
                ? `q${id}`
                : type === 'daily'
                ? `d${id}`
                : type === undefined
                ? `w${id}`
                : `e${id}`
        },
        changeScreenMobile: function(type) {
            this.screenMobile = type
        },
        onResize() {
            this.windowWidth = window.innerWidth
            if (this.$refs.profile.clientHeight !== this.commonHeight)
                this.matchHeight()
        },
        matchHeight() {
            if (this.windowWidth > 768) {
                this.commonHeight = this.$refs.profile.clientHeight + 'px'
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.profile-wrapper {
    box-sizing: border-box;
    display: flex;

    .profile-mobile-nav {
        display: none;
        justify-content: center;
        align-items: center;
        margin: 10px 0;

        &__btn {
            width: 110px;
            padding: 8px 12px;
            background-color: transparent;
            border: 2px solid $basic-background;
            color: $basic-background;
            font-size: 14px;
            cursor: pointer;
        }

        .left-btn {
            border-top-left-radius: 5px;
            border-bottom-left-radius: 5px;
        }

        .right-btn {
            border-top-right-radius: 5px;
            border-bottom-right-radius: 5px;
        }

        .active {
            background-color: $basic-background;
            color: $basic-white;
        }
    }

    .column-wrap {
        padding-top: 90px;
        box-sizing: border-box;
        .profile {
            box-sizing: border-box;
            height: 100%;
            max-height: 1500px;
            background-color: #fff;
            box-sizing: border-box;

            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 25px 20px 0 20px;

            &__main-info {
                display: flex;
                flex-direction: column;
                align-items: center;
                &__photo {
                    width: 270px;
                    height: 320px;
                    border: 1px solid rgb(179, 179, 179);
                    flex-shrink: 0.5;
                    position: relative;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;
                    .img {
                        display: block;
                        width: 100%;
                        height: 100%;
                        object-fit: cover;
                        position: absolute;
                        top: 0;
                        left: 0;
                    }
                }
                &__text {
                    .text__name {
                        font-size: 24px;
                        text-align: center;
                        font-weight: 400;
                        line-height: 16px;
                        color: $basic-black;
                        margin-top: 22px;

                        &__patronymic {
                            display: none;
                        }
                    }

                    .text__department {
                        color: $brand-gray-dark;
                        margin-top: 16px;
                        text-align: center;
                    }

                    .text__bio {
                        font-size: 18px;
                        color: $brand-night;
                        line-height: 20px;
                        margin-top: 21px;
                    }
                    .text__level {
                        display: none;
                    }
                }
            }

            .profile__stats {
                display: flex;
                width: 100%;
                justify-content: space-between;
                margin-top: 20px;
                flex-wrap: wrap;

                &-item {
                    display: flex;
                    align-items: center;
                }

                &-icon {
                    width: 30px;
                    height: 30px;
                }

                &-value {
                    font-size: 18px;
                    margin-left: 3px;
                }

                .coins {
                    color: $text-color-yellow;
                }

                .lightnings {
                    color: $text-color-green;
                }

                .hearts {
                    color: $text-color-red;
                }
            }
            .task-props {
                width: 100%;
                .profile__task {
                    width: 100%;
                    margin-top: 15px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;

                    &-title {
                        color: $basic-background;
                        font-size: 18px;
                        line-height: 16px;
                        width: 100%;
                    }

                    &-name {
                        font-size: 20px;
                        color: $basic-black;
                        line-height: 16px;
                        margin: 0;
                        margin-top: 8px;
                        margin-bottom: 17px;
                        width: 100%;
                    }

                    &-deadline {
                        width: 100%;
                        margin-top: 13px;
                        color: $basic-black;
                        font-size: 16px;
                        line-height: 16px;

                        .gray-txt {
                            color: $basic-background;
                        }
                        .progress {
                            display: none;
                        }
                    }
                }
                .profile__props {
                    width: 100%;
                    display: flex;
                    justify-content: space-between;
                    flex-direction: column;

                    &-row {
                        font-size: 16px;
                        line-height: 16px;
                        margin-top: 15px;

                        &-title {
                            width: 155px;
                        }

                        &-value {
                            font-size: 22px;
                            width: 60px;
                        }

                        &-light {
                            font-size: 14px;
                            line-height: 16px;
                            color: $brand-gray-dark;
                        }
                    }
                }
            }
        }

        .tasks {
            box-sizing: border-box;
            height: 100%;
            overflow-y: auto;
            padding: 25px 20px 0 20px;
            min-width: 412px;

            &__title {
                font-size: 18px;
                font-weight: 400;
                line-height: 16px;
                color: $brand-gray-dark;
                margin: 0;
                margin-bottom: 35px;
            }

            &__item:not(:first-child) {
                margin-top: 30px;
            }
        }

        .achievements {
            height: 100%;
            box-sizing: border-box;
            padding: 25px 20px 0 20px;
            overflow-y: auto;

            &__title {
                font-size: 18px;
                font-weight: 400;
                line-height: 16px;
                color: $brand-gray-dark;
                margin: 0;
                margin-bottom: 35px;
            }

            &__inner {
                display: flex;
                justify-content: flex-start;
                flex-wrap: wrap;

                &-item {
                    width: 110px;
                    height: 110px;
                    border-radius: 50%;
                    background-color: #f7d9b9;
                    margin: 0 30px 30px 0;
                    position: relative;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    overflow: hidden;

                    &__image {
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
            }
        }
    }
    .wrap {
        &__profile {
            max-width: 450px;
            flex: 1 0 0;
        }
        &__tasks,
        &__achieves {
            height: 100vh;
            flex: 1 1 0;
        }
    }

    .hide {
        display: none;
    }
}

@media (max-height: $media-breakpoint-sm-height) {
    .profile-wrapper {
        .column-wrap {
            .profile {
                &__main-info {
                    &__photo {
                        height: 300px;
                    }
                    &__text {
                        .text__name {
                            font-size: 22px;
                            margin-top: 10px;
                        }

                        .text__bio {
                            font-size: 17px;
                            margin-top: 10px;
                        }
                    }
                }
            }
        }
    }
}

@media (max-width: $media-breakpoint-lg) {
    .profile-wrapper {
        .column-wrap {
            .profile {
                padding: 20px 15px 0 15px;

                &__main-info {
                    &__photo {
                        height: 300px;
                    }
                    &__text {
                        .text__name {
                            font-size: 22px;
                            margin-top: 20px;
                        }

                        .text__department {
                            margin-top: 12px;
                        }

                        .text__bio {
                            font-size: 17px;
                            margin-top: 15px;
                        }
                    }
                }
                .task-props {
                    .profile__task {
                        margin-top: 15px;

                        &-title {
                            font-size: 17px;
                        }

                        &-name {
                            font-size: 18px;
                        }

                        &-deadline {
                            margin-top: 10px;
                        }
                    }
                    .profile__props {
                        &-row {
                            font-size: 16px;
                            line-height: 16px;
                            margin-top: 20px;

                            &-title {
                                width: 130px;
                            }

                            &-value {
                                font-size: 18px;
                                width: 40px;
                            }

                            &-light {
                                font-size: 12px;
                                line-height: 16px;
                                text-align: right;
                            }
                        }
                    }
                }
            }

            .achievements {
                &__inner {
                    &-item {
                        width: 65px;
                        height: 65px;
                        margin: 0 20px 20px 0;
                    }
                }
            }
        }
    }
}

@media (max-width: $media-breakpoint-md) {
    .profile-wrapper {
        .column-wrap {
            padding-top: 80px;
        }
    }
}

@media (max-width: $media-breakpoint-sm) {
    .profile-wrapper {
        padding-top: 100px;
        min-height: 100vh;
        height: auto;
        flex-direction: column;
        justify-content: flex-start;

        .profile-mobile-nav {
            margin-top: 20px;
            display: flex;
        }
        .wrap {
            &__profile {
                max-width: none;
                flex: none;
                padding-top: 0;
            }
            &__tasks,
            &__achieves {
                height: auto;
                flex: none;
                max-width: none;
                padding-top: 0;
            }
        }
        .column-wrap {
            .profile {
                background-color: transparent;
                width: 100%;
                &__main-info {
                    width: 100%;
                    flex-direction: row;
                    justify-content: space-between;
                    align-items: flex-start;
                    &__photo {
                        width: 150px;
                        height: 150px;
                        flex-shrink: 0;
                        border-radius: 50%;
                        padding: 10px;
                        overflow: hidden;
                        border: 6px solid transparent;
                        background: linear-gradient(
                                179.8deg,
                                #3281a0 0.17%,
                                #74e5ea 117.9%
                            )
                            border-box;

                        .img {
                            box-sizing: border-box;
                            border: 6px solid $basic-grey;
                            border-radius: 50%;
                        }
                    }
                    &__text {
                        width: 100%;

                        .text__name {
                            font-size: 18px;
                            color: $basic-black;
                            margin-top: 30px;

                            &__patronymic {
                                display: inline;
                            }
                        }
                        .text__bio {
                            display: none;
                        }
                        .text__level {
                            margin-top: 12px;
                            width: 100%;
                            display: inline-block;
                            text-align: center;

                            &__count {
                                font-weight: bold;
                            }
                        }
                    }
                }
                .profile__stats {
                    display: none;
                }
                .task-props {
                    display: flex;
                    flex-direction: column-reverse;
                    .profile__props {
                        margin-top: 10px;
                        border: 2px solid $basic-background;
                        box-sizing: border-box;
                        border-radius: 10px;
                        padding: 5px;
                        &-row {
                            margin: 5px 0;
                        }
                        .level {
                            display: none;
                        }
                    }
                    .profile__task {
                        .profile__task-name {
                            margin-bottom: 5px;
                        }
                        .progress-bar {
                            display: none;
                        }
                        &-deadline {
                            margin-top: 0;
                            .progress {
                                display: inline;
                                margin-right: 10px;
                            }
                        }
                    }
                }
            }
            .tasks,
            .achievements {
                padding: 10px 10px 0 10px;
                padding-bottom: 65px;
                min-width: auto;
                max-width: none;
                width: 100%;
                overflow-y: initial;
            }
        }
    }
}

@media (max-width: $media-breakpoint-xs) {
    .profile-wrapper {
        .column-wrap {
            .profile {
                &__main-info {
                    &__photo {
                        width: 95px;
                        height: 95px;
                    }
                    &__text {
                        width: 100%;

                        .text__name {
                            margin-top: 10px;
                        }
                    }
                }
            }
        }
    }
}
</style>
