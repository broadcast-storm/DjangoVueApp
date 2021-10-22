<template>
    <div class="shop__state">
        <div class="shop__user-stats">
            <div class="stats__coins-value">
                На счету:<span class="coin">
                    <CoinSvg class="item-icon" />{{ user.stats['coins'] }}</span
                >
            </div>
            <div class="stats__level">Текущий уровень: {{ user.level }}</div>
        </div>
        <router-link class="shop__cart" to="/shop/cart">
            Корзина<CartSvg class="cart-icon" />
            <span v-if="cart.length != 0" class="cart-number">{{
                cart.length
            }}</span>
        </router-link>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import CartSvg from '@/assets/icons/cart.svg'
import { mapGetters } from 'vuex'
export default {
    components: {
        CoinSvg,
        CartSvg,
    },
    data() {
        return {
            user: Object.assign({}, this.$store.getters.getUserData),
        }
    },
    computed: {
        ...mapGetters(['getUserData']),
        ...mapGetters('cart', ['getCart']),
        cart: function() {
            return this.getCart
        },
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.item-icon {
    height: 34px;
    width: 34px;
    padding-right: 4px;
}
.shop {
    &__state {
        position: fixed;
        display: flex;
        flex-direction: column;
        margin-left: 10px;
        .shop__user-stats {
            background-color: #fff;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            padding: 14px 0 25px 24px;
            margin-bottom: 34px;
            font-size: 24px;
            line-height: 16px;
            // margin-right: 28px;
            .stats {
                &__coins-value,
                &__level {
                    display: flex;
                    align-items: center;
                    color: #545969;
                }
                &__coins-value {
                    padding-bottom: 15px;
                    .coin {
                        display: flex;
                        align-items: center;
                        padding-left: 24px;
                        color: #f2af49;
                        padding-right: 23px;
                    }
                }
            }
        }
        .shop__cart {
            background-color: #fff;
            box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
            padding: 13px 24px 8.5px;
            height: 62px;
            display: flex;
            align-items: center;
            width: 276px;
            font-size: 24px;
            line-height: 16px;
            color: #545969;
            text-decoration: none;
            cursor: pointer;
            .cart-number {
                position: absolute;
                width: 24px;
                height: 24px;
                bottom: 31px;
                left: 156px;
                margin-left: 75px;
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 20px;
                line-height: 16px;
                color: #fff;
                background-color: #26bcc2;
                border-radius: 30px;
            }
            .cart-icon {
                width: 59.4px;
                height: 60px;
                margin-left: 80px;
                padding-left: 4px;
            }
        }
    }
}
</style>
