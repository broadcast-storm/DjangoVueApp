<template>
    <div class="competition">
        <div class="competition__search">
            <div>
                <div class="search__item">
                    <label for="competitions__input">Поиск соперника </label>
                </div>
                <div class="search__input">
                    <input
                        id="competitions__input"
                        v-model="search"
                        class="input__item"
                        type="text"
                        placeholder="Имя и Фамилия"
                    />
                    <SearchSvg class="input__svg" />
                </div>
            </div>
        </div>
        <div
            v-for='user in users'
            :key="user.id"
            class="competition__user"
        >
            <div class="user__profile">
                <div class="profile__image">
                    <img
                        src='https://sun9-83.userapi.com/impf/c638620/v638620169/b968c/e-VX7of7gXw.jpg?size=600x600&quality=96&sign=70d85cfa4ef50ccbb84ffb9cf57725d5&type=album'
                        class="user-image"
                        alt=""
                    />
                </div>
                <div class="profile__information">
                    <div class="information__name">
                        <h3 class="information__title">
                            {{user.name}} {{user.surname}}
                        </h3>
                        <p class="information__subtitle">
                            состоит в команде {{user.team}}
                        </p>
                    </div>
                    <div class="information__description">
                        <p class="information__indicator">
                            Продуктивность
                            <span class="desctiption-bold">{{user.productivity}}%</span>
                        </p>
                        <p class="information__indicator">
                            Качество
                            <span class="desctiption-bold">{{user.quality}}%</span>
                        </p>
                        <p class="information__indicator">
                            Текущий уровень
                            <span class="desctiption-bold">{{user.level}}%</span>
                        </p>
                    </div>
                </div>
            </div>
            <div class="user__actions">
                <button @click="openWindow(user.name,user.surname)">Начать соревнование</button>
            </div>
        </div>
        <!-- КОНЕЦ СОРЕВНОВАНИЯ -->
        <ModalCompetitions :status='status' :name='modalData' @close='openWindow' />
    </div>
</template>

<script>
import SearchSvg from '@/assets/icons/search.svg'
import ModalCompetitions from '@/components/ModalCompetitions'
import { USERS_REQUEST_FETCHING } from '@/store/action-types/users'
import { mapGetters, mapActions } from 'vuex'

export default {
    name: 'Competitions',
    components: {
        SearchSvg,
        ModalCompetitions,
    },
    // props: ['search'],
    data() {
        return {
            status: false,
            test_page: false,
            search: '',
            modalData:'Sur',
        }
    },
    computed: {
        ...mapGetters('users', ['getUsers']),
        users() {
            console.log(this.$route.query.query)
            return this.getUsers.filter(user=>{
                let name = user.name + ' ' + user.surname
                return name.toLowerCase().includes(this.search.toLowerCase())
            })
        }
    },
    async mounted() {
        this.search=this.$route.query.query,
        await this.USERS_REQUEST_FETCHING()
    },
    methods: {
        ...mapActions('users', [USERS_REQUEST_FETCHING]),
        openWindow: function(name,surname) {
            this.status = !this.status,
            this.modalData = name + ' ' + surname
        },
    },
}
</script>

<style lang="scss" scoped>
.header {
    &__text {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 10vh;
        color: #545969;
    }
}
.profile {
    &__information {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        font-size: 18px;
        margin-left: 20px;
    }
}
.user {
    &__profile {
        display: flex;
        flex-direction: row;
    }
    &__actions {
        margin-top: 20px;
        button {
            cursor: pointer;
            width: 449px;
            padding: 5.5px 0;
            background-color: #5f66a9;
            border: none;
            color: white;
            font-size: 24px;
            border-radius: 8px;
            box-shadow: 0 5px 5px gray;
        }
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
        font-size: 18px;
        line-height: 18px;
        margin-top: 10px;
        color: #7d849a;
    }
}
.indicators {
    display: flex;
    &__title {
        font-weight: 700;
        font-size: 18px;
        color: #545969;
    }
    &__image {
        margin-right: 12px;
        width: 40px;
    }
}
.competition {
    margin-left: 100px;
    margin-right: 90px;
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    margin-top: 89px;
    overflow-y: auto;
    height: calc(100vh - 90px);
    &__search {
        display: flex;
        justify-content: space-between;
        margin-top: 20px;
    }
    &__indicator {
        display: flex;
        align-items: center;
        font-style: normal;
        font-weight: 400;
        font-size: 24px;
        margin-right: 15px;
        color: #1a2740;
        span {
            margin-right: 30px;
            &:last-child {
                margin-right: 0;
            }
        }
        &:last-child {
            margin-right: 0;
        }
    }
    &__title {
        font-size: 24px;
        color: #545969;
        font-weight: 700;
        margin-bottom: 10px;
    }
    &__about {
        margin-top: 50px;
    }
    &__myCompetition {
        margin-top: 40px;
    }
    &__control {
        margin-top: 30px;
        display: flex;
        justify-content: space-between;
    }
    &__user {
        margin-top: 50px;
    }
}
.myCompetition {
    &__table {
        width: 100%;
        font-size: 18px;
        border-collapse: separate;
        border-spacing: 0 2px;
        .table__row {
            background-color: #f0f3fe;
            .row__id {
                color: #545969;
            }
        }
        thead {
            .table__row {
                margin-top: 2px;
                th {
                    text-align: left;
                    padding: 23px 13px;
                }
            }
        }
        tbody {
            .table__row {
                td {
                    margin-top: 2px;
                    padding: 1px 13px 7px 13px;
                    .competition__logo {
                        width: 42px;
                        margin-right: 20px;
                    }
                }
                .row__logo {
                    display: flex;
                    align-items: center;
                }
                .row__enemy {
                    vertical-align: middle;
                    .enemy__logo {
                        vertical-align: middle;
                        margin-right: 15px;
                        width: 24px;
                        height: 24px;
                        border-radius: 100px;
                    }
                }
                .row__result p {
                    padding: 2px 10px;
                    width: 120px;
                    max-width: 90px;
                    text-align: center;
                    border-radius: 5px;
                    border: 1px solid #7fc008;
                }
                .result__win p {
                    color: #7fc008;
                }
                .result__losing p {
                    border-color: #db303f;
                    color: #db303f;
                }
                .result__draw p {
                    color: #db8c28;
                    border-color: #db8c28;
                }
            }
        }
    }
}
.about {
    &__description {
        color: #4c4f56;
        padding: 8px 13px;
        border: 1px solid #545969;
    }
}
.search {
    &__item {
        color: #545969;
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-size: 18px;
        line-height: 18px;
        color: #545969;
        label {
            font-weight: 700;
        }
    }

    &__input {
        width: 650px;
        position: relative;
        margin-top: 12px;
    }
}
.control {
    &__pages {
        display: flex;
        align-items: center;
        button {
            cursor: pointer;
            color: #b0bac9;
            border: 1px solid #b0bac9;
            background-color: white;
            padding: 9px 12px 7px 12px;
            border-radius: 6px;
            img {
                height: 15px;
            }
        }
        div {
            display: flex;
            align-items: center;
            width: 80px;
            justify-content: space-around;
            margin: 0 12px;
            font-size: 14px;
            color: #b0bac9;
            input {
                color: #26bcc2;
                height: 34px;
                border: 1px solid #b0bac9;
                text-align: center;
                width: 35px;
            }
            input::-webkit-outer-spin-button,
            input::-webkit-inner-spin-button {
                -webkit-appearance: none;
                margin: 0;
            }
            .select__pages {
                color: black;
            }
        }
    }
    &__pagesCount {
        display: flex;
        color: #454d59;
        align-items: center;
        font-size: 14px;
        input {
            margin-left: 20px;
            height: 34px;
            border: 1px solid #b0bac9;
            padding: 0 10px;
            width: 40px;
        }
    }
}
.input {
    &__item {
        //font-family: HelveticaNeueCyr;
        font-style: normal;
        font-weight: 100 !important;
        font-size: 18px;
        line-height: 18px;
        color: #545969;
        border: 0;
        width: 650px;
        height: 33px;
        padding-left: 27px;
        outline: none;
        &:hover {
            cursor: pointer;
        }
        &::placeholder {
            font-weight: 100;
            color: #8e9ac0;
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
    background: #5f66a9;
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
    background: #5f66a9;
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
