<template>
  <div class="auth-container"><router-view name="auth-router" /></div>
</template>

<script>
export default {
  name: "Auth"
};
</script>

<style lang="scss" scoped>
.auth-container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-color: $basic-grey;
  background-image: url("~@/assets/img/auth/background.jpg");
  background-attachment: fixed;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}
</style>
