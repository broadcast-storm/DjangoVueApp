<template>
  <div class="header-container">
    <h1 class="header-container__page-name">Профиль</h1>
    <div class="header-container__user-statistics">
      <div>
        <CoinSvg />
        <span>{{ statistics.coins }}</span>
      </div>
      <div>
        <LightningSvg />
        <span>{{ statistics.lightnings }}</span>
      </div>
      <div>
        <HeartSvg />
        <span>{{ statistics.hearts }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import CoinSvg from "@/assets/icons/coin.svg";
import HeartSvg from "@/assets/icons/heart.svg";
import LightningSvg from "@/assets/icons/lightning.svg";
export default {
  name: "Header",
  components: { CoinSvg, HeartSvg, LightningSvg },
  props: {
    statistics: {
      type: Object,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped>
.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 30px 90px;
  border: 1px solid #b1b2b7;
  &__page-name {
    font-size: 24px;
    line-height: 28px;
    color: $brand-night;
  }

  &__user-statistics {
    display: flex;
  }
}
</style>
