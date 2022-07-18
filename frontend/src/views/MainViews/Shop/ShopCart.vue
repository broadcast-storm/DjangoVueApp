<template>
    <div class="cart-wrapper">
        <div v-if="cart.length == 0" class="cart__cleared">
            <div class="cart__header">
                <div class="cart__back-block">
                    <div class="cart__arrow">←</div>
                    <router-link to="/shop/" class="cart__back"
                        >Вернуться к покупкам</router-link
                    >
                </div>
                <h2 v-if="!status" class="cart__headline">Корзина</h2>
            </div>
            <div class="cart__cleared-status">
                <h3 v-if="status" class="items-bought">Товары куплены</h3>
                <p v-if="status" class="items-information">
                    Получить ты их можешь у Деда Мороза
                </p>
                <p v-if="!status" class="items-information">
                    В корзине нет товаров
                </p>
            </div>
        </div>
        <div v-if="cart.length != 0" class="cart__list">
            <div class="cart__header">
                <div class="cart__back-block">
                    <div class="cart__arrow">←</div>
                    <router-link to="/shop/" class="cart__back"
                        >Вернуться к покупкам</router-link
                    >
                </div>
                <h2 v-if="!status" class="cart__headline">Корзина</h2>
            </div>
            <div v-for="item in items" :key="item.id" class="shop__item">
                <div class="shop__item-img">
                    <div class="img"></div>
                </div>
                <div class="shop__item-description">
                    <h3 class="item-headline">{{ item.product.title }}</h3>
                    <span class="item-description">{{
                        item.product.description
                    }}</span>
                    <span class="item-value"
                        >{{ item.money }}<CoinSvg class="item-icon"
                    /></span>
                    <span class="item-required_level"
                        >требуемый уровень: {{ item.level }}</span
                    >
                </div>
            </div>
        </div>
        <div v-if="cart.length != 0" class="cart__state">
            <button class="cart__clear" @click="clearCar()">
                Очистить корзину
            </button>
            <div class="cart__state-card">
                <h3 class="card-headline">Итого</h3>
                <span class="card-number">{{ cart.length }} товара</span>
                <span class="card-value"
                    >{{ cartSumm }}<CoinSvg class="item-icon"
                /></span>
                <button
                    class="card-buy"
                    @click="
                        clearCar()
                        buy()
                    "
                >
                    Оплатить<Arrow class="arrow" />
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import CoinSvg from '@/assets/icons/coin.svg'
import Arrow from '@/assets/icons/arrow-rigth.svg'

import { mapGetters } from 'vuex'
import { mapMutations } from 'vuex'
export default {
    components: {
        CoinSvg,
        Arrow,
    },
    data() {
        return {
            status: false,
        }
    },
    computed: {
        ...mapGetters('items', ['getItems']),
        ...mapGetters('cart', ['getCart']),
        items: function() {
            let items = this.getItems.data
            let cart = this.getCart
            return items.filter(a => cart.filter(b => b.id == a.id).length != 0)
        },
        cart: function() {
            return this.getCart
        },
        cartSumm: function() {
            let summ = 0
            for (let i of this.items) {
                summ += i.money
            }
            return summ
        },
    },
    methods: {
        ...mapMutations(['clearCart']),
        clearCar: function() {
            this.$store.commit('cart/clearCart')
        },
        buy: function() {
            this.status = true
        },
    },
}
</script>

<style lang="scss" scoped>
@import url('./ShopCart.css');
</style>
