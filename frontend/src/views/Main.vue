<template>
  <div class="main-container">
    <Header :statistics="stats" />
    <router-view name="main-router" />
  </div>
</template>

<script>
import Header from "@/components/Header";
import { stats } from "@/mocks/headerStats";
export default {
  name: "Main",
  components: { Header },
  data() {
    return {
      stats
    };
  }
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
