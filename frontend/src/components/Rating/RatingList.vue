<template>
    <div class="rating-table">
        <div class="row">
            <div v-for="raiting in ratings" :key="raiting.id" class="row__item">
                <RatingItem :rating="raiting" />
            </div>
        </div>
    </div>
</template>

<script>
import RatingItem from './RatingItem'

export default {
    name: 'RatingList',
    components: { RatingItem },
    props: {
        ratings: {
            type: Array,
            default: () => [],
        },
    },
}
</script>

<style lang="scss" scoped>
.rating-table {
    margin-left: 70px;
    margin-right: 14px;
}
.row__item {
    display: flex;
    max-height: 88px;
    max-width: 75%;
    margin: 17px 0;
    background: #fff;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}
</style>
