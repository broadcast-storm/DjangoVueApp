<template>
  <div>
    <h1>{{ headerText }}</h1>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {
    headerText: {
      type: String,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped></style>
