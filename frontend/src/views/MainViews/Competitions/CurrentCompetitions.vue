<template>
    <div class="competition-wrapper">
        <!-- НАЧАЛО СОРЕВНОВАНИЯ -->
        <div class="competition-header">
            <div class="header__text">
                <h3>Текущие соревнование</h3>
                <h3>Бой телепузиков</h3>
            </div>
        </div>
        <div class="competition-content">
            <div class="content__block">
                <div class="profile">
                    <div class="profile__image">
                        <img
                            src="@/mocks/UserPhoto.jpg"
                            class="user-image"
                            alt=""
                        />
                    </div>
                    <div class="profile__information">
                        <div class="information__name">
                            <h3>Александра Пушкина</h3>
                            <p>состоит в команде ВКЦэхи</p>
                        </div>
                        <div class="information__description">
                            <p>
                                Продуктивность
                                <span class="desctiption-bold">85%</span>
                            </p>
                            <p>
                                Качество
                                <span class="desctiption-bold">85%</span>
                            </p>
                            <p>
                                Текущий уровень
                                <span class="desctiption-bold">85%</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="content__split">
                <h1>VS</h1>
            </div>
            <div class="content__block">
                <div class="profile">
                    <div class="profile__image">
                        <img
                            src="@/mocks/UserPhoto.jpg"
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
                                Качество
                                <span class="desctiption-bold">85%</span>
                            </p>
                            <p>
                                Текущий уровень
                                <span class="desctiption-bold">85%</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- КОНЕЦ СОРЕВНОВАНИЯ -->
    </div>
</template>

<script>
export default {
    components: {},
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
.competition-wrapper {
    display: flex;
    flex-direction: column;
    margin-top: 90px;
    flex-wrap: wrap;
    width: 100%;
    overflow-y: auto;
    height: calc(100vh - 90px);
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
}
.search__input input:focus ~ .input__hint {
    opacity: 0;
    transition: 0.3s;
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
    right: calc(100% - 51%);
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
    color: #1a2740;
}
.information__name h3 {
    color: #545969;
    font-weight: bold;
}
.information__name p {
    color: #7d849a;
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
}
.competition-button p {
    color: white;
    font-weight: bold;
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
}
.window-button p {
    color: white;
    font-size: 24px;
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
