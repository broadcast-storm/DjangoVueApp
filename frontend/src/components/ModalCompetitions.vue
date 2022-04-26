<template>
    <!-- НАЧАЛО ОКНО ДЛЯ СОЗДАНИЯ СОРЕВНОВАНИЯ -->
    <div v-if="status" class="competition__window">
        <div class="window">
            <div class="window__title">
                <ExitSvg class="window__exit__button" @click='close' />
                <h2>Вы и {{name}} начинаете новое соревнование</h2>
            </div>
            <div class="window__body">
                <label for="competition__name">Введите название</label>
                <input
                    id="competition__name"
                    type="text"
                    class="window__input"
                    placeholder="Битва магов"
                />
                <label for="competition__criterior">Выберите критерий</label>
                <div class='criteriorButtons'>
                    <input
                        id="criterior1"
                        type="radio"
                        class="window__input input__criterior"
                        text="Битва магов"
                        value='quality'
                        v-model="criterior"
                    />
                    <label class='criterior__label' :class="[criterior==='quality'?'active':'']" for="criterior1">Качество</label>
                    <input
                        id="criterior2"
                        type="radio"
                        class="window__input input__criterior"
                        text="Битва магов"
                        value='productivity'
                        v-model="criterior"
                    />  
                    <label class='criterior__label' :class="[criterior==='productivity'?'active':'']" for="criterior2">Продуктивность</label>
                </div>
                <label for="competition__rate">Ваша ставка</label>
                <select
                    id="competition__rate"
                    type="text"
                    class="window__select"
                >
                    <option value="productivity">Монетки</option>
                    <option value="quality">Энергия</option>
                    <option value="level">Жизни</option>
                </select>
                <label for="competition__name">Количество</label>
                <input
                    id="competition__name"
                    type="text"
                    class="window__input"
                    placeholder="100"
                />

            </div>
            <button class="window__button" @click="startCompetition()">
                Создать
            </button>
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
        status: Boolean,
        name: String
    },
    data() {
        return {
            test_page: false,
            user: '',
            criterior: 'quality',
        }
    },
    methods: {
        startCompetition: function() {
            this.status = !this.status
            this.$router.push(routesList.competitionsPage.path)
            localStorage.setItem('versus', true)
        },
        close() {
            this.$emit('close');
        }
    }
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
    padding-bottom: 25px;
    input[type='radio'] {
        display: none;
    }
    input::placeholder{
        color: #9BA2B9
    }
    &__input, &__select,.criterior__label {
        border: 1px solid #C1C6E8;
        padding-left: 15px;
        border-radius: 10px;
        color:#545969;
    }
    &__input {
        width: 446px;
        height: 33px;
        
    }
    .criteriorButtons {
        display: flex;
        justify-content: space-between;
        .input__criterior {
            // display: none;
        }
        .criterior__label {
            width: 40%;
            text-align: center;
            background-color: white;
            padding: 5px 0 5px 0;
            border-width: 2px;
        }
        .active {
            color: #4753BF;
            border: 2px solid #4753BF;
            box-shadow: 0 0 7px rgba(128, 128, 128, 0.612);
        }
    }
    &__select {
        width: 466px;
        height: 33px;
        color: #545969;
        option {
            color: #545969
        }
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
        label {
            padding-top: 10px;
            padding-bottom: 5px;
            color: #545969;
        }
    }
    &__button {
        margin-top: 15px;
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
}
</style>
