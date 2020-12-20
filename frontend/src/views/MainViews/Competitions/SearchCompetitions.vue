<template>
    <div class="competition-wrapper">
        <!-- ПОИСК -->
        <div class="competition__search">
            <div class="search__item">
                <p>Поиск соперника</p>
            </div>
            <div class="search__input">
                <input
                    v-model="user"
                    class="input__item"
                    type="text"
                    placeholder="Имя и Фамилия"
                />
                <SearchSvg class="input__svg" />
            </div>
        </div>
        <!-- КОНЕЦ ПОИСКА -->
        <!-- НАЧАЛО ПРОФИЛЯ -->
        <div class="competition-profile">
            <div class="profile">
                <div class="profile__image">
                    <img
                        src="@/assets/img/competitions/UserPhoto.jpg"
                        class="user-image"
                        alt=""
                    />
                </div>
                <div class="profile__information">
                    <div class="information__name">
                        <h3 class="information__title">Джонатан Смирнов</h3>
                        <p class="information__subtitle">
                            состоит в команде Пирожков
                        </p>
                    </div>
                    <div class="information__description">
                        <p class="information__indicator">
                            Продуктивность
                            <span class="desctiption-bold">85%</span>
                        </p>
                        <p class="information__indicator">
                            Качество <span class="desctiption-bold">85%</span>
                        </p>
                        <p class="information__indicator">
                            Текущий уровень
                            <span class="desctiption-bold">85%</span>
                        </p>
                    </div>
                </div>
            </div>
            <button class="competition-button" @click="openWindow()">
                Начать соревнование
            </button>
        </div>
        <!-- КОНЕЦ ПОИСКА -->
        <ModalCompetitions :status="status" />
    </div>
</template>

<script>
import SearchSvg from '@/assets/icons/search.svg'
//import ExitSvg from '@/assets/icons/exit.svg'
import ModalCompetitions from '@/components/ModalCompetitions'

export default {
    name: 'Competitions',
    components: {
        SearchSvg,
        ModalCompetitions,
        //ExitSvg,
    },
    props: {},
    data() {
        return {
            status: false,
            test_page: false,
            user: '',
        }
    },
    methods: {
        openWindow: function() {
            this.status = !this.status
        },
    },
}
</script>

<style lang="scss" scoped>
.competition-wrapper {
    display: flex;
    flex-direction: column;
    margin-top: 90px;
    flex-wrap: wrap;
    width: 100%;
    overflow-y: auto;
    height: calc(100vh - 90px);
}
.competition-header {
    margin-left: 20px;
    margin-top: 40px;
}
.header {
    &__text {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 10vh;
        color: #545969;
    }
}
.competition-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 85%;
    margin-left: 20px;
    margin-top: 40px;
}
.content {
    &__block {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 502px;
        height: 287px;
        border: 1px solid #545969;
    }

    &__split {
        font-weight: bold;
        font-size: 48px;
        color: #545969;
    }
}
.profile {
    display: flex;

    &__information {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        margin-left: 20px;
    }
}
.user-image {
    width: 171px;
}
.information {
    &__description {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        min-height: 50%;
    }
    &__title {
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-weight: 550;
        font-size: 24px;
        line-height: 24px;
        color: #545969;
    }
    &__subtitle {
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-weight: 550;
        font-size: 18px;
        line-height: 18px;
        margin-top: 10px;
        color: #7d849a;
    }
    &__indicator {
        //font-family: Helvetica;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        color: #1a2740;
    }
}
.desctiption-bold {
    font-weight: bold;
    color: #1a2740;
}
.competition {
    &__search {
        margin-left: 100px;
        margin-top: 20px;
    }
}
.search {
    &__item {
        color: #545969;
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-weight: 550;
        font-size: 18px;
        line-height: 18px;
        color: #545969;
    }

    &__input {
        width: 650px;
        position: relative;
        margin-top: 12px;
    }
}
.input {
    &__item {
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 18px;
        color: #d8dcea;
        border: 0;
        width: 650px;
        height: 33px;
        padding-left: 30px;
        outline: none;
        &:hover {
            cursor: pointer;
        }
        &:focus ~ .input__hint {
            opacity: 0;
            transition: 0.3s;
        }
    }
    &__svg {
        position: absolute;
        z-index: 1;
        top: 0;
        right: 0;
        width: 23px;
        &:hover {
            cursor: pointer;
        }
    }
    &__hint {
        position: absolute;
        z-index: 1;
        top: 8.25px;
        left: 30px;
        opacity: 0.21;
    }
}
.competition-profile {
    display: flex;
    flex-direction: column;
    margin-top: 40px;
    flex-wrap: wrap;
    margin-left: 100px;
    margin-top: 20px;
}

.competition-button {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #26bcc2;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    width: 449px;
    height: 39px;
    margin-top: 20px;
    color: white;
    font-size: 24px;
    border: 0;
}
.competition-button:hover {
    cursor: pointer;
}
.competition-window {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.65);
    width: 100%;
    height: 100%;
    z-index: 999999;
}
.window {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    padding: 10px;
    background: #d8dcea;
    width: 480px;
    height: 296px;
    &__input {
        width: 446px;
        height: 33px;
    }
}
.window-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 95%;
}
.window-exit {
    &__button {
        width: 12px;
        &:hover {
            cursor: pointer;
        }
    }
}
.window-body {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    height: 30%;
    &__input {
        border: 0;
        outline: none;
    }
}
.window-button {
    display: flex;
    justify-content: center;
    align-items: center;
    background: #26bcc2;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    border-radius: 8px;
    width: 249px;
    height: 34px;
    font-size: 24px;
    color: white;
    border: 0;
    outline: none;
    &:hover {
        cursor: pointer;
    }
}
</style>
