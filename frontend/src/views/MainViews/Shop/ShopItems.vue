<template
    ><div class="center">
        <div class="wrapper">
            <ShopState />
            <div class="shop">
                <form class="filters">
                    <div class="filter_text">Поиск:</div>
                    <input class="input_item_find" type="text" />
                    <div class="filter_text">Цена:</div>
                    <div class="price-inp">
                        <span class="filter_text_c">От</span>
                        <input type="number" class="input_item" />
                    </div>
                    <div class="price-inp">
                        <span class="filter_text_c">До</span>
                        <input type="number" class="input_item" />
                    </div>
                    <button
                        class="filter_button"
                        type="button"
                        @click="assignValues()"
                    >
                        Применить
                    </button>
                </form>
                <div class="shop__items">
                    <div class="shop__instruments">
                        Сортировать:

                        <div
                            class="instruments-selection"
                            :class="{
                                instruments_active: instruments == true,
                            }"
                        >
                            <div
                                id="1"
                                class="instruments__sorting-method"
                                @click=";(sort = 'ascendingValue'), target('1')"
                            >
                                по возрастанию цены
                            </div>
                            <div
                                id="2"
                                class="instruments__sorting-method"
                                @click="
                                    ;(sort = 'descendingValue'), target('2')
                                "
                            >
                                по убыванию цены
                            </div>
                            <div
                                id="3"
                                class="instruments__sorting-method"
                                @click=";(sort = 'ascendingLevel'), target('3')"
                            >
                                по возрастанию уровня
                            </div>
                            <div
                                id="4"
                                class="instruments__sorting-method"
                                @click="
                                    ;(sort = 'descendingLevel'), target('4')
                                "
                            >
                                по убыванию уровня
                            </div>
                        </div>
                    </div>
                    <div class="grid-items">
                        <div v-for="item in orderedItems" :key="item.id">
                            <div class="card">
                                <div class="front">
                                    <div class="img">
                                        <img :src="item.product.photo" alt="" />
                                    </div>
                                    <div class="shop__item-description">
                                        <div class="item-headline">
                                            {{ item.product.title }}
                                        </div>
                                        <div class="item-required_level">
                                            требуемый уровень: {{ item.level }}
                                        </div>
                                        <div class="money-info">
                                            <div class="item-value">
                                                {{ item.money
                                                }}<CoinSvg class="item-icon" />
                                            </div>
                                            <div class="item-lower">
                                                <button class="item-cart">
                                                    <CartSvg
                                                        v-if="
                                                            cart.filter(
                                                                a =>
                                                                    a.id ==
                                                                    item.id
                                                            ).length == 0
                                                        "
                                                        class="item-cart_icon"
                                                        @click="
                                                            addToCart(item.id)
                                                        "
                                                    />
                                                    <CheckMark
                                                        v-if="
                                                            cart.filter(
                                                                a =>
                                                                    a.id ==
                                                                    item.id
                                                            ).length != 0
                                                        "
                                                        class="item-cart_icon"
                                                    />
                                                </button>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="back">
                                    <div class="back__desc">
                                        {{ item.product.description }}
                                    </div>
                                    <div class="money-info">
                                        <div class="item-value">
                                            {{ item.money
                                            }}<CoinSvg class="item-icon" />
                                        </div>
                                        <div class="item-lower">
                                            <button class="item-cart">
                                                <CartSvg
                                                    v-if="
                                                        cart.filter(
                                                            a => a.id == item.id
                                                        ).length == 0
                                                    "
                                                    class="item-cart_icon"
                                                    @click="addToCart(item.id)"
                                                />
                                                <CheckMark
                                                    v-if="
                                                        cart.filter(
                                                            a => a.id == item.id
                                                        ).length != 0
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
import { mapActions } from 'vuex'

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
            maxPrice: 99999,
            minPrice: 0,
            searchText: '',
            sort: 'ascendingValue',
            pageNumber: 0,
            size: 10,
        }
    },
    computed: {
        ...mapGetters('items', ['getItems']),
        ...mapGetters('cart', ['getCart']),
        orderedItems: function() {
            const { searchText } = this
            let c = this.getItems.data
            console.log(c)
            // eslint-disable-next-line prettier/prettier
            if (c != null) {
                c = c.filter(
                    p => p.money >= this.minPrice && p.money <= this.maxPrice
                )
                // eslint-disable-next-line prettier/prettier
                c = c.filter(
                    p =>
                        p.product.title
                            .toLowerCase()
                            .indexOf(searchText.toLowerCase()) !== -1
                )

                switch (this.sort) {
                    case 'ascendingValue':
                        c = c.sort((a, b) => (a.money > b.money ? 1 : -1))

                        break
                    case 'descendingValue':
                        c = c.sort((a, b) => (a.money < b.money ? 1 : -1))

                        break
                    case 'ascendingLevel':
                        c = c.sort((a, b) => (a.level > b.level ? 1 : -1))

                        break
                    case 'descendingLevel':
                        c = c.sort((a, b) => (a.level < b.level ? 1 : -1))
                        break
                }
            }

            return c
        },
        cart: function() {
            return this.getCart
        },
        items: function() {
            return this.getItems
        },
    },

    mounted() {
        this.ITEMS_REQUEST()
        console.log(this.getItems)
    },
    methods: {
        ...mapActions('items', ['ITEMS_REQUEST']),
        ...mapMutations(['addToCart']),
        addToCart: function(itemId) {
            this.$store.commit('cart/addToCart', { id: itemId })
        },
        getLink: function(itemId) {
            return '/shop/item/' + itemId
        },
        assignValues: function() {
            var text = document.getElementsByTagName('input')[0]
            var min = document.getElementsByTagName('input')[1]
            var max = document.getElementsByTagName('input')[2]
            if (min.value == 0) {
                min.value = 1
            }
            if (max.value == 0) {
                max.value = 99999
            }
            if (text.value == 0) {
                text.value = ''
            }
            this.maxPrice = max.value
            this.minPrice = min.value
            this.searchText = text.value
        },
        target: function(x) {
            document.getElementById('1').classList.remove('target_sort')
            document.getElementById('2').classList.remove('target_sort')
            document.getElementById('3').classList.remove('target_sort')
            document.getElementById('4').classList.remove('target_sort')
            document.getElementById(x).classList.add('target_sort')
        },
    },
}
</script>

<style lang="scss" scoped>
@import url('./ShopItems.css');
</style>
