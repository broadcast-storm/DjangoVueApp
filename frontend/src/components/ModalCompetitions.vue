<template>
    <!-- НАЧАЛО ОКНО ДЛЯ СОЗДАНИЯ СОРЕВНОВАНИЯ -->
    <div v-if="status" class="competition__window">
        <div class="window">
            <div class="window__title">
                <ExitSvg class="window__exit__button"/>
                <h2>Вы и Джонатан Смирнов начинаете новое соревнование</h2>
            </div>
            <div class="window__body">
                <label for='competition__name'>Введите название</label>
                <input id='competition__name' type="text" class="window__input" />
                <label for='competition__criterion'>Выберите критерий</label>
                <select id='competition__criterion' type="text" class="window__select">
                    <option value="productivity">Продуктивность</option>
                    <option value="quality">Качество</option>
                    <option value="level">Текущий уровень</option>
                </select>
            </div>
            <button @click="startCompetition()"  class="window__button" >Создать</button>
        </div>
    </div>
    <!-- КОНЕЦ СОРЕВНОВАНИЯ -->
</template>

<script>
import ExitSvg from '@/assets/icons/exit.svg'
import routesList from '@/router/routesList'
export default {
    name: 'Modal',
    components: {
        ExitSvg,
    },
    props: {
        status: {
            default: false,
            type: Boolean,
        },
    },
    data() {
        return {
            test_page: false,
            user: '',
        }
    },
    methods: {
        startCompetition: function() {
            this.status = !this.status
            this.$router.push(routesList.competitionsPage.path)
            localStorage.setItem('versus',true)
        },
    },
}
</script>

<style lang="scss" scoped>
.competition__window {
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
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background: #d8dcea;
    width: 480px;
    height: 306px;
    padding-bottom: 25px;
    &__input {
        width: 446px;
        height: 33px;
        border: none;
        padding-left: 20px;
    }
    &__select {
        width: 466px;
        height: 33px;
        border: none;
        padding-left: 20px;
    }
    &__title {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: flex-end;
        width: 95%;
        h2 {
            text-align: center;
        }
    }
    &__exit {
        &__button {
            width: 16px;
            height: 16px;
            &:hover {
                cursor: pointer;
            }
        }
    }
    &__body {
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        height: 50%;
        &__input {
            border: 0;
            outline: none;
        }
    }
    &__button {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #5F66A9;
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
}
</style>
