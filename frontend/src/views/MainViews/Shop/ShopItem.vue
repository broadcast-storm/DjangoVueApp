<template>
    <div class="shop-wrapper">
        <ShopState />
        <div class="shop__item-wrapper">
            <div class="shop__item">
                <div class="shop__item-img">
                    <img :src="item.img" alt="" />
                </div>
                <div class="shop__item-description">
                    <h2 class="item-headline">
                        {{ item.name }}
                    </h2>
                    <span class="item-required_level"
                        >требуемый уровень: {{ item.level }}</span
                    >
                    <span class="item-description">{{ item.description }}</span>
                    <span class="item-value"
                        ><CoinSvg class="item-icon" />{{ item.value }}</span
                    >
                    <button
                        v-if="cart.filter(a => a.id == item.id).length == 0"
                        class="item-cart"
                        @click="addToCart(item.id)"
                    >
                        <CartSvg class="item-cart_icon" /><span
                            class="item-cart_text"
                            >В корзину</span
                        >
                    </button>
                    <button
                        v-if="cart.filter(a => a.id == item.id).length != 0"
                        class="item-cart item-cart_added"
                    >
                        <CheckMark class="item-cart_icon" /><span
                            class="item-cart_text"
                            >Добавлено</span
                        >
                    </button>
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

import ShopState from '@/components/ShopState'
import { mapMutations } from 'vuex'
export default {
    components: {
        CoinSvg,
        CartSvg,
        CheckMark,
        ShopState,
    },
    props: ['id'],
    computed: {
        ...mapGetters('items', ['getItems']),
        ...mapGetters('cart', ['getCart']),
        cart: function() {
            return this.getCart
        },
        item: function() {
            return this.getItems.filter(itemId => itemId.id == this.id)[0]
        },
    },
    methods: {
        ...mapMutations(['addToCart']),
        addToCart: function(itemId) {
            this.$store.commit('cart/addToCart', { id: itemId })
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
    width: 100%;
    overflow-y: auto;
}
.item-icon {
    height: 34px;
    width: 34px;
    padding-right: 4px;
}
.shop {
    &__item-wrapper {
        margin-left: 333px;
        height: calc(100vh - 90px);
    }
    &__item {
        background: #fff;
        box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.25),
            -2px 4px 8px rgba(0, 0, 0, 0.25);
        display: flex;
        &-img {
            padding: 66px 30px 82px 35px;
            img {
                height: 221px;
                width: 221px;
                border-radius: 8px;
            }
        }
        &-description {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            .item {
                &-headline {
                    font-size: 36px;
                    line-height: 16px;
                    color: #1a2740;
                    margin-top: 75px;
                }
                &-required_level {
                    margin-top: 25px;
                    margin-bottom: 20px;
                    font-size: 18px;
                    line-height: 16px;
                    color: #7d849a;
                }
                &-description {
                    font-size: 18px;
                    line-height: 16px;
                    color: #545969;
                    width: 350px;
                    margin-right: 90px;
                }
                &-value {
                    font-size: 36px;
                    line-height: 16px;
                    color: #f2af49;
                    display: flex;
                    align-items: center;
                    padding-top: 17px;
                    padding-bottom: 22px;
                    .item-icon {
                        width: 46px;
                        height: 46px;
                    }
                }
                &-cart {
                    font-size: 24px;
                    line-height: 16px;
                    background: #26bcc2;
                    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                    border-radius: 5px;
                    border: none;
                    display: flex;
                    align-items: center;
                    align-self: flex-end;
                    height: 36px;
                    width: 174px;
                    margin-right: 36px;
                    margin-bottom: 24px;
                    padding-left: 11px;
                    color: #fff;
                    outline: none;
                    cursor: pointer;
                    &_icon {
                        width: 29.06px;
                        height: 26.16px;
                        path {
                            fill: #fff;
                        }
                    }
                    &_text {
                        padding-left: 12.5px;
                    }
                    &_added {
                        width: 184px;
                    }
                }
            }
        }
    }
}
</style>
