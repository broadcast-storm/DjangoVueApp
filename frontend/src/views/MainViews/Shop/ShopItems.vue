<template>
    <div class="shop-wrapper">
        <ShopState />
        <div class="shop__items">
            <div class="shop__instruments">
                Сортировать:
                <span
                    class="shop__instruments-selection"
                    @click="
                        instruments
                            ? (instruments = false)
                            : (instruments = true)
                    "
                    >{{ currentInstrument }}</span
                >
                <div
                    class="instruments-selection"
                    :class="{
                        instruments_active: instruments == true,
                    }"
                >
                    <div
                        class="instruments__sorting-method"
                        @click="
                            ;(sort = 'ascendingValue'), (instruments = false)
                        "
                    >
                        по возрастанию цены
                    </div>
                    <div
                        class="instruments__sorting-method"
                        @click="
                            ;(sort = 'descendingValue'), (instruments = false)
                        "
                    >
                        по убыванию цены
                    </div>
                    <div
                        class="instruments__sorting-method"
                        @click="
                            ;(sort = 'ascendingLevel'), (instruments = false)
                        "
                    >
                        по возрастанию уровня
                    </div>
                    <div
                        class="instruments__sorting-method"
                        @click="
                            ;(sort = 'descendingLevel'), (instruments = false)
                        "
                    >
                        по убыванию уровня
                    </div>
                </div>
            </div>
            <div v-for="item in orderedItems" :key="item.id">
                <div class="shop__item">
                    <div class="shop__item-img">
                        <img :src="item.img" alt="" />
                    </div>
                    <div class="shop__item-description">
                        <h2 class="item-headline">
                            <router-link
                                class="item-headline_link"
                                :to="getLink(item.id)"
                                exact
                                >{{ item.name }}</router-link
                            >
                        </h2>
                        <span class="item-description">{{
                            item.description
                        }}</span>
                        <span class="item-value"
                            >{{ item.value }}<CoinSvg class="item-icon"
                        /></span>
                        <div class="item-lower">
                            <span class="item-required_level"
                                >требуемый уровень: {{ item.level }}</span
                            >
                            <button class="item-cart">
                                <CartSvg
                                    v-if="
                                        cart.filter(a => a.id == item.id)
                                            .length == 0
                                    "
                                    class="item-cart_icon"
                                    @click="addToCart(item.id)"
                                />
                                <CheckMark
                                    v-if="
                                        cart.filter(a => a.id == item.id)
                                            .length != 0
                                    "
                                    class="item-cart_icon"
                                />
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import CartSvg from '@/assets/icons/cart.svg'
import CheckMark from '@/assets/icons/mark.svg'

import { mapGetters } from 'vuex'
import { mapMutations } from 'vuex'

import ShopState from '@/components/ShopState'
export default {
    components: {
        CoinSvg,
        CartSvg,
        CheckMark,
        ShopState,
    },
    data() {
        return {
            items: Object.assign([], this.$store.getters.getItems),
            sort: 'ascendingValue',
            instruments: false,
        }
    },
    computed: {
        ...mapGetters(['getItems']),
        ...mapGetters(['getCart']),
        orderedItems: function() {
            let c = this.items
            switch (this.sort) {
                case 'ascendingValue':
                    c = c.sort((a, b) => (a.value > b.value ? 1 : -1))
                    break
                case 'descendingValue':
                    c = c.sort((a, b) => (a.value < b.value ? 1 : -1))
                    break
                case 'ascendingLevel':
                    c = c.sort((a, b) => (a.level > b.level ? 1 : -1))
                    break
                case 'descendingLevel':
                    c = c.sort((a, b) => (a.level < b.level ? 1 : -1))
                    break
            }
            return c
        },
        currentInstrument: function() {
            let c
            switch (this.sort) {
                case 'ascendingValue':
                    c = 'по возрастанию цены'
                    break
                case 'descendingValue':
                    c = 'по убыванию цены'
                    break
                case 'ascendingLevel':
                    c = 'по возрастанию уровня'
                    break
                case 'descendingLevel':
                    c = 'по убыванию уровня'
                    break
            }
            return c
        },
        cart: function() {
            return Object.assign([], this.$store.getters.getCart)
        },
    },
    methods: {
        ...mapMutations(['addToCart']),
        addToCart: function(itemId) {
            this.$store.commit('addToCart', { id: itemId })
        },
        getLink: function(itemId) {
            return '/shop/item/' + itemId
        },
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.shop-wrapper {
    display: flex;
    flex-direction: row;
    margin-top: 90px;
    flex-wrap: wrap;
    width: 100%;
    overflow-y: auto;
}
.item-icon {
    height: 34px;
    width: 34px;
    padding-right: 4px;
}
.shop {
    &__items {
        margin-left: 318px;
        height: calc(100vh - 90px);
        .shop__instruments {
            background: #ffffff;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            padding: 10px 0 10px 13px;
            font-size: 18px;
            line-height: 16px;
            margin-bottom: 20px;
            position: fixed;
            width: 822px;
            -webkit-touch-callout: none;
            -webkit-user-select: none;
            -khtml-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            &-selection {
                color: #4c62b4;
                cursor: pointer;
            }
            .instruments-selection {
                display: none;
                margin-left: 117.55px;
                .instruments__sorting-method {
                    padding-top: 10px;
                    &:hover {
                        color: #4c62b4;
                        cursor: pointer;
                    }
                }
            }
            .instruments_active {
                display: block;
            }
        }
        > :nth-child(2) {
            margin-top: 73px;
        }
        .shop__item {
            margin-top: 22px;
            background: #ffffff;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            display: flex;
            width: 822px;
            &-img {
                padding: 16px 24px 15px 32px;
                img {
                    width: 176px;
                    height: 176px;
                    border-radius: 8px;
                }
            }
            &-description {
                display: flex;
                flex-direction: column;
                padding-top: 21px;
                width: 100%;
                .item-headline {
                    font-size: 36px;
                    line-height: 16px;
                    padding-bottom: 24px;
                    &_link {
                        text-decoration: none;
                        color: #1a2740;
                    }
                }
                .item-description {
                    width: 340px;
                    font-size: 18px;
                    line-height: 16px;
                    color: #545969;
                }
                .item-value {
                    display: flex;
                    align-items: center;
                    justify-content: flex-end;
                    padding-right: 30px;
                    font-size: 36px;
                    line-height: 16px;
                    color: #1a2740;
                    padding-bottom: 20px;
                }
                .item-lower {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-bottom: 15px;
                    padding-right: 19px;
                    .item-required_level {
                        font-size: 18px;
                        line-height: 16px;
                        color: #545969;
                    }
                    .item-cart {
                        width: 52px;
                        height: 52px;
                        border-radius: 100px;
                        border: none;
                        outline: none;
                        background: #26bcc2;
                        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                        cursor: pointer;
                        &_icon {
                            width: 29.06px;
                            height: 26.16px;
                            path {
                                fill: #fff;
                            }
                        }
                    }
                }
            }
        }
    }
}
</style>
