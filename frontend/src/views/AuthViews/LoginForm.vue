<template>
    <div class="login-container">
        <LogoSvg class="login-container__logo" :regular-color="'#3281a0'" />
        <form class="login-form" @submit.prevent="login">
            <div class="login-form__alert-container">
                <p v-if="!incorrectAuth" class="login-form__alert-text">
                    Войдите, чтобы продолжить
                </p>
                <p v-else class="login-form__alert-text error">
                    Неверный логин или пароль
                </p>
            </div>
            <input
                v-model="username"
                type="text"
                required
                class="login-form__input"
                placeholder="Логин"
            />
            <input
                v-model="password"
                type="password"
                required
                class="login-form__input"
                placeholder="Пароль"
            />
            <div class="login-form__link-container">
                <router-link
                    :to="routesList.authPage.children.forgotpasswordPage.path"
                    class="login-form__link-text"
                >
                    Напомнить пароль
                </router-link>
            </div>
            <button type="submit" class="login-form__button">
                <Spinner
                    v-if="$store.state.tokens.status === 'loading'"
                    :size="20"
                    :line-bg-color="'#b1b2b7'"
                    :line-fg-color="'#ffffff'"
                />
                <span v-else>Войти</span>
            </button>
        </form>
    </div>
</template>

<script>
import LogoSvg from '@/components/LogoSvg'
import routesList from '@/router/routesList'
import { AUTH_REQUEST } from '@/store/actions/tokens'
import Spinner from 'vue-simple-spinner'

export default {
    name: 'LoginForm',
    components: { LogoSvg, Spinner },
    data() {
        return {
            routesList,
            incorrectAuth: false,
            username: '',
            password: '',
        }
    },
    methods: {
        async login() {
            try {
                await this.$store.dispatch(AUTH_REQUEST, {
                    username: this.username,
                    password: this.password,
                })
                this.$router.push(routesList.mainPage.path)
            } catch (error) {
                console.log(error)
                this.incorrectAuth = true
            }
        },
    },
}
</script>

<style lang="scss" scoped>
.login-container {
    box-sizing: border-box;
    max-width: 600px;
    width: 100%;
    padding: 30px;
    min-height: 365px;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    background: #ffffff;
    box-shadow: 7px 8px 8px rgba(0, 0, 0, 0.25),
        -15px -8px 9px rgba(87, 87, 87, 0.3);

    &__logo {
        max-width: 100px;
        width: 100%;
        margin-bottom: 20px;
    }

    .login-form {
        width: 80%;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: left;

        &__alert-container,
        &__link-container {
            width: 100%;
            text-align: left;
        }

        &__alert-text {
            font-size: 14px;
            line-height: 24px;
            color: $brand-gray;
        }
        .error {
            color: red;
        }

        &__input {
            font-size: 14px;
            width: 100%;
            height: 38px;
            border: 1px solid $basic-background;
            box-sizing: border-box;
            border-radius: 6px;
            margin: 10px 0;
            padding: 5px 10px;
            color: $brand-night;
        }

        &__link-text {
            font-size: 14px;
            line-height: 17px;
            text-decoration-line: underline;
            color: #283c62;
        }

        &__button {
            font-size: 14px;
            margin-top: 20px;
            width: 100%;
            border: none;
            height: 38px;
            background: $btn-main-blue;
            border-radius: 6px;
            color: $basic-white;
            cursor: pointer;
        }
    }
}
</style>
