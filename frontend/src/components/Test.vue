<template>
    <div class="test">
        <h3 class="test-headline">
            {{ testInfo.title }}
        </h3>
        <div class="test-wrap">
            <span class="test-description">{{ testInfo.description }}</span
            ><router-link class="test-begin-btn" :to="getLink(testInfo.id)">
                Начать <Arrow class="arrow" />
            </router-link>
        </div>
    </div>
</template>

<script>
import Arrow from '@/assets/icons/arrow-rigth.svg'

export default {
    name: 'Test',
    components: {
        Arrow,
    },
    props: {
        testInfo: {
            type: Object,
            default: () => {},
        },
    },
    methods: {
        getLink: function(testId) {
            return '/tests/' + testId
        },
    },
}
</script>

<style lang="scss" scoped>
.test {
    background: #ffffff;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    margin-bottom: 17px;
    padding: 15px;
    box-sizing: border-box;
    &-headline {
        font-size: 18px;
        color: #1a2740;
    }
    &-wrap {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin-top: 10px;
        .test-description {
            font-size: 14px;
            color: #7d849a;
            max-width: 300px;
        }
        .test-begin-btn {
            box-sizing: border-box;
            background: #26bcc2;
            border-radius: 5px;
            font-size: 14px;
            color: #fff;
            border: none;
            outline: none;
            height: 22px;
            padding: 0 10px 0 15px;
            width: 100px;
            align-self: flex-end;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-decoration: none;
            cursor: pointer;
            .arrow {
                width: 10px;
                height: 19px;
            }
        }
    }
}
</style>
