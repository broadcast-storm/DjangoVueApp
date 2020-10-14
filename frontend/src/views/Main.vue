<template>
  <div class="main-container">
    <Header />
    <router-view name="main-router" />
  </div>
</template>

<script>
import Header from "@/components/Header";
export default {
  name: "Main",
  components: { Header }
};
</script>

<style lang="scss">
.main-container {
  box-sizing: border-box;
  width: 100%;
  height: 100vh;
  background-color: $basic-grey;
}
</style>
