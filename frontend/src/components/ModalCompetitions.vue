<template>
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
            <button class="window-button">Создать</button>
        </div>
    </div>
    <!-- КОНЕЦ СОРЕВНОВАНИЯ -->
</template>

<script>
import ExitSvg from '@/assets/icons/exit.svg'
export default {
    components: {
        ExitSvg,
    },
    name: 'Modal',
    props: {},
    data() {
        return {
            status: false,
            test_page: false,
            user: '',
        }
    },
    methods: {
        openWindow: function () {
            this.status = !this.status
        },
    },
}
</script>

<style lang="scss" scoped>
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