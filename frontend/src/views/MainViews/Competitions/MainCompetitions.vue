<template>
    <div class="competition">
        <!-- ПОИСК -->
        <div class="competition__search">
            <div>
                <div class="search__item">
                    <label for='competitions__input'>Поиск соперника</label>
                </div>
                <div class="search__input">
                    <input
                        id = 'competitions__input'
                        v-model="user"
                        class="input__item"
                        type="text"
                        placeholder="Имя и Фамилия"
                    />
                    <SearchSvg @click="openWindow()" class="input__svg" />
                </div>
            </div>
            <div class="competition__indicators">
                <h3 class='indicators__title'>Мои показатели:</h3>
                <div class='indicators'>
                    <p class="competition__indicator">
                        <img class='indicators__image' src="@/assets/img/competitions/indicator__productivity.png" alt="img">
                        <span>85%</span>
                    </p>
                    <p class="competition__indicator">
                        <img class='indicators__image' src="@/assets/img/competitions/indicator__quality.png" alt="img">
                        <span>75</span>
                    </p>
                    <p class="competition__indicator">
                        <img class='indicators__image' src="@/assets/img/competitions/indicator__level.png" alt="img">
                        <span>88</span>
                    </p>
                </div>
            </div>
        </div>
        <div class="competition__about">
            <h2 class="about__title competition__title">Как проходят соревнования?</h2>
            <p class="about__description">Lorem ipsum, dolor sit amet consectetur adipisicing elit. In, iste maiores sint, unde soluta sed explicabo necessitatibus ipsa veniam ipsum ipsam hic deserunt accusantium quasi ad quam aliquam ea itaque, molestiae iure! Dolor nostrum harum maiores officiis minima pariatur praesentium atque repellat natus. Excepturi nulla mollitia iure tempore. Voluptatem deserunt est quos beatae quasi debitis, maiores quibusdam asperiores numquam laborum totam necessitatibus illum quis sequi voluptatibus impedit optio, ducimus explicabo vel. Soluta nemo eum assumenda blanditiis, quaerat culpa corporis voluptatem itaque, amet ipsam vero doloremque qui hic illo saepe laboriosam. Temporibus accusantium laborum ea fuga similique dicta nisi minima nobis.</p>
        </div>
        <div class="competition__myCompetition">
            <h2 class="myCompetition__title competition__title">Мои соревнования</h2>
            <table class="myCompetition__table">
                <thead>
                    <tr class="table__row">
                        <th class="row__id">#</th>
                        <th class="">Соревнование</th>
                        <th class="">Исход</th>
                        <th class="">Критерий</th>
                        <th class="">Показатель</th>
                        <th class="">Противник</th>
                        <th class="">Выигрыш</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="table__row">
                        <td class="row__id">
                            1
                        </td>
                        <td class="row__logo">
                            <img class='competition__logo' src="@/assets/img/competitions/competition__logo.jpg" alt="logo">
                            Бой телепузиков
                        </td>
                        <td class="row__result result__win">
                            <p>Выигрыш</p>
                        </td>
                        <td class="">
                            Продуктивность
                        </td>
                        <td class="">
                            88 vs 67
                        </td>
                        <td class="row__enemy">
                            <img class='enemy__logo' src="@/assets/img/competitions/enemy__logo.jpg" alt="pht">
                            Evan Flores
                        </td>
                        <td class="">
                            $452.85
                        </td>
                    </tr>
                    <tr class="table__row">
                        <td class="row__id">
                            2
                        </td>
                        <td class="row__logo">
                            <img class='competition__logo' src="@/assets/img/competitions/competition__logo.jpg" alt="logo">
                            Бой телепузиков
                        </td>
                        <td class="row__result result__losing">
                            <p>Проигрыш</p>
                        </td>
                        <td class="">
                            Качество
                        </td>
                        <td class="">
                            13 vs 67
                        </td>
                        <td class="row__enemy">
                            <img class='enemy__logo' src="@/assets/img/competitions/enemy__logo.jpg" alt="pht">
                            Steven Flores
                        </td>
                        <td class="">
                            $412.85
                        </td>
                    </tr>
                    <tr class="table__row">
                        <td class="row__id">
                            3
                        </td>
                        <td class="row__logo">
                            <img class='competition__logo' src="@/assets/img/competitions/competition__logo.jpg" alt="logo">
                            Атака ведьм
                        </td>
                        <td class="row__result result__draw">
                            <p>Ничья</p>
                        </td>
                        <td class="">
                            Уровень
                        </td>
                        <td class="">
                            13 vs 67
                        </td>
                        <td class="row__enemy">
                            <img class='enemy__logo' src="@/assets/img/competitions/enemy__logo.jpg" alt="pht">
                            Steven Flores
                        </td>
                        <td class="">
                            $412.85
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class='competition__control'>
            <div class="control__pages">
                <button><img src="@/assets/img/competitions/arrow__left.png" alt="arrow left"></button>
                <div>
                    <input type=number value='1' class='select__page'>
                    /
                    <span class='select__pages'>10</span></div>
                <button><img src="@/assets/img/competitions/arrow__right.png" alt="arrow riht"></button>
            </div>
            <div class="control__pagesCount">
                <label for='pagesCount'>Показывать на странице</label>
                <input id='pagesCount' type="number" value='6'>
            </div>
        </div>
        <!-- <div class="competition-profile">
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
                </div>
            </div>
            <button class="competition-button" @click="openWindow()">
                Начать соревнование
            </button>
        </div> -->
        <ModalCompetitions :status="status" />
    </div>
</template>

<script>
import SearchSvg from '@/assets/icons/search.svg'
//import ExitSvg from '@/assets/icons/exit.svg'
import ModalCompetitions from '@/components/ModalCompetitions'
import routesList from '@/router/routesList'

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
            this.$router.push(routesList.competitionsPage.path + '/' + routesList.competitionsPage.children.SearchCompetitions.path)
        },
    },
}
</script>

<style lang="scss" scoped>
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
}
.indicators {
    display: flex;
    margin-top: 12px;
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
        color: #1A2740;
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
}
.myCompetition {
    &__table {
        width: 100%;
        font-size: 18px;
        border-collapse: separate;
        border-spacing: 0 2px;
        .table__row {
            background-color: #F0F3FE;
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
                    border: 1px solid #7FC008;
                }
                .result__win p {
                    color: #7FC008
                }
                .result__losing p{
                    border-color: #DB303F;
                    color: #DB303F;
                }
                .result__draw p {
                    color: #DB8C28;
                    border-color: #DB8C28;
                }
            }
        }
    }
}
.about {
    &__description {
        color: #4C4F56;
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
            color:#B0BAC9;
            border: 1px solid #B0BAC9;
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
            color: #B0BAC9;
            input {
                color:#26BCC2;
                height: 34px;
                border: 1px solid #B0BAC9;
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
        color:#454D59;
        align-items: center;
        font-size: 14px;
            input {
                margin-left: 20px;
                height: 34px;
                border: 1px solid #B0BAC9;
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
        color: #8E9AC0;
        border: 0;
        width: 650px;
        height: 33px;
        padding-left: 27px;
        outline: none;
        &:hover {
            cursor: pointer;
        }
        &::placeholder{
            font-weight: 100;
            color: #8E9AC0;
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

