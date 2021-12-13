<template>
    <div class="rating-table">
        <div class="row">
            <div
                v-for="(raiting, index) in sortedRatings"
                :key="index"
                class="row__item"
            >
                <RatingItem :index="index" :rating="raiting" :sort="sort" />
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
        sort: {
            type: String,
            default: 'month',
        },
    },
    computed: {
        sortedRatings: function() {
            let c = this.ratings
            switch (this.sort) {
                case 'month':
                    c = c.sort((a, b) => b.ratingMonth - a.ratingMonth)
                    break
                case 'day':
                    c = c.sort((a, b) => b.ratingDay - a.ratingDay)
                    break
                case 'week':
                    c = c.sort((a, b) => b.ratingWeek - a.ratingWeek)
                    break
            }
            return c
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
