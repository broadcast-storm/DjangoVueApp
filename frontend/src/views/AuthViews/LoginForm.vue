<template>
  <div class="login-container">
    <LogoSvg class="login-container__logo" :regular-color="'#3281a0'" />
    <form action="" class="login-form">
      <div class="login-form__alert-container">
        <p class="login-form__alert-text">Войдите, чтобы продолжить</p>
      </div>
      <input
        type="text"
        required
        class="login-form__input"
        placeholder="Логин"
      />
      <input
        type="password"
        required
        class="login-form__input"
        placeholder="Пароль"
      />
      <div class="login-form__link-container">
        <router-link to="/auth/forgot-password" class="login-form__link-text">
          Напомнить пароль
        </router-link>
      </div>
      <button type="submit" class="login-form__button">Войти</button>
    </form>
  </div>
</template>

<script>
import LogoSvg from "@/components/LogoSvg";
export default {
  name: "LoginForm",
  components: { LogoSvg }
};
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

    &__input {
      width: 100%;
      height: 38px;
      border: 1px solid $basic-background;
      box-sizing: border-box;
      border-radius: 6px;
      margin: 10px 0;
      padding: 5px 10px;
      color: $brand-gray;
    }

    &__link-text {
      font-size: 12px;
      line-height: 17px;
      text-decoration-line: underline;
      color: #283c62;
    }

    &__button {
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
