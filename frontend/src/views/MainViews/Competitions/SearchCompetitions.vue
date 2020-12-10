<template>
    <div class="competition-wrapper">
        <!-- ПОИСК -->
        <div class="competition__search">
            <div class="search__item">
                <p>Поиск соперника</p>
            </div>
            <div class="search__input">
                <input type="text" placeholder="Имя и Фамилия" v-model="user" />
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
                        <h3>Джонатан Смирнов</h3>
                        <p>состоит в команде Пирожков</p>
                    </div>
                    <div class="information__description">
                        <p>
                            Продуктивность
                            <span class="desctiption-bold">85%</span>
                        </p>
                        <p>
                            Качество <span class="desctiption-bold">85%</span>
                        </p>
                        <p>
                            Текущий уровень
                            <span class="desctiption-bold">85%</span>
                        </p>
                    </div>
                </div>
            </div>
            <button v-on:click="openWindow()" class="competition-button">
                Начать соревнование
            </button>
        </div>
        <!-- КОНЕЦ ПОИСКА -->
        <!-- НАЧАЛО ОКНО ДЛЯ СОЗДАНИЯ СОРЕВНОВАНИЯ -->
        <div v-if="status" class="competition-window">
            <div class="window">
                <div class="window-title">
                    <h2>Новое соревнование</h2>
                    <ExitSvg
                        v-on:click="openWindow()"
                        class="window-exit__button"
                    />
                </div>
                <div class="window-body">
                    <p>Введите название соревнования</p>
                    <input type="text" class="window__input" />
                </div>
                <button class="window-button">
                    Создать
                </button>
            </div>
        </div>
        <!-- КОНЕЦ СОРЕВНОВАНИЯ -->
    </div>
</template>

<script>
import SearchSvg from '@/assets/icons/search.svg'
import ExitSvg from '@/assets/icons/exit.svg'

export default {
    components: {
        SearchSvg,
        ExitSvg,
    },
    name: 'Competitions',
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
@font-face {
font-family: 'HelveticaNeueCyr';
src: url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Light.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Medium.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-UltraLightItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Black.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-BlackItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Bold.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-BoldItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Heavy.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-HeavyItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Italic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Light.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-LightItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Medium.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-MediumItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Roman.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-Thin.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-ThinItalic.woff') format('woff'),
url('~@/assets/fonts/HelveticaNeueCyr/HelveticaNeueCyr-UltraLight.woff') format('woff'),


}
.competition-wrapper {
    display: flex;
    flex-direction: column;
    margin-top: 90px;
    flex-wrap: wrap;
    width: 100%;
    overflow-y: auto;
    height: calc(100vh - 90px);
}
.search__input {
    width: 650px;
}
.search__input input {
    border: 0;
    width: 650px;
    height: 33px;
    padding-left: 30px;
    outline: none;
}
.search__item {
    color: #545969;
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: 550;
    font-size: 18px;
    line-height: 18px;
    color: #545969;
}
.search__input input:focus ~ .input__hint {
    opacity: 0;
    transition: 0.3s;
}
.search__input input::-webkit-input-placeholder {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: #d8dcea;
}
.search__input input::-moz-placeholder {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: #d8dcea;
}
.search__input input:-moz-placeholder {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: #d8dcea;
}
.search__input input:-ms-input-placeholder {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: #d8dcea;
}
.competition__search,
.competition-profile {
    margin-left: 100px;
    margin-top: 20px;
}
.search__input {
    position: relative;
    margin-top: 12px;
}
.input__hint {
    position: absolute;
    z-index: 1;
    top: 8.25px;
    left: 30px;
    opacity: 0.21;
}
.input__svg {
    position: absolute;
    z-index: 1;
    top: 0;
    right: 0;
    width: 23px;
}
.input__svg:hover {
    cursor: pointer;
}
.competition-profile {
    display: flex;
    flex-direction: column;
    margin-top: 40px;
    flex-wrap: wrap;
}
.profile {
    display: flex;
}
.user-image {
    width: 171px;
}
.profile__information {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    margin-left: 20px;
}
.information__description {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    min-height: 50%;
}
.information__description p {
    font-family: Helvetica;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    color: #1a2740;
}
.information__name h3 {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    font-weight: 550;
    font-size: 24px;
    line-height: 24px;
    color: #545969;
}
.information__name p {
    font-family: HelveticaNeueCyr;
    font-style: normal;
    margin-top: 10px;
    font-weight: 550;
    font-size: 18px;
    line-height: 18px;
    color: #7D849A;
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
}
button {
    border: 0;
    outline: none;
}
.competition-button:hover {
    cursor: pointer;
}
button:hover {
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
}
.window__input {
    width: 446px;
    height: 33px;
}
.window-exit__button {
    width: 12px;
}
.window-exit__button:hover {
    cursor: pointer;
}
.window-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 95%;
}
.window-body {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    height: 30%;
}
.window-body input {
    border: 0;
    outline: none;
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
}
.desctiption-bold {
    font-weight: bold;
    color: #1a2740;
}

// SPLIT

.competition-header,
.competition-content {
    margin-left: 20px;
    margin-top: 40px;
}
.competition-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 85%;
}
.header__text {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 10vh;
    color: #545969;
}
.content__block {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 502px;
    height: 287px;
    border: 1px solid #545969;
}
.content__split {
    font-weight: bold;
    font-size: 48px;
    color: #545969;
}
</style>
