<template>
    <div class="shop__user-stats">
        <div class="stats__level">Текущий уровень: {{ user.level }}</div>
        <div class="animation">
            <router-link class="shop__cart" to="/shop/cart">
                Корзина<CartSvg class="cart-icon" />
                <span v-if="cart.length != 0" class="cart-number">{{
                    cart.length
                }}</span>
            </router-link>
        </div>
    </div>
</template>

<script>
import CartSvg from '@/assets/icons/cart.svg'
import { mapGetters } from 'vuex'
export default {
    components: {
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
@import url('https://fonts.googleapis.com/css2?family=Advent+Pro:wght@600&display=swap');
* {
    box-sizing: border-box;
}
.animation :hover {
    border: 2px solid #4c62b4;
    overflow: hidden;
    cursor: pointer;
}
.shop__user-stats {
    position: relative;
    width: 1300px;
    justify-content: space-between;
    display: flex;
    font-size: 24px;
    line-height: 16px;
    .stats {
        &__level {
            font-family: 'Advent Pro', sans-serif;
            font-weight: bold;
            color: #545969;
            display: flex;
            align-items: center;
            color: #545969;
        }
    }
}
.shop__cart {
    border: 2px solid #fff;
    justify-content: space-between;
    border-radius: 8px;
    background-color: #fff;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    padding: 10px 19px 8.5px 13px;
    height: 53px;
    display: flex;
    flex: 0 0 auto;
    align-items: center;
    width: 175px;
    font-size: 24px;
    line-height: 53px;
    color: #545969;
    text-decoration: none;
}
.shop__cart :hover {
    border: initial;
}

.cart-number {
    position: absolute;
    width: 25px;
    height: 25px;
    bottom: 24px;
    left: 1260px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    line-height: 16px;
    color: #fff;
    background-color: #5f66a9;
    border-radius: 30px;
}
.cart-icon {
    width: 37px;
    height: 37px;
}
</style>
