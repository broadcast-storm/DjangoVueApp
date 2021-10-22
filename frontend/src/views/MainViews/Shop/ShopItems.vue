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
                <span class="span_class">Товаров на странице: </span>
                <input v-model="size" class="input_item_size" type="number" />
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
            <div v-for="item in paginatedData" :key="item.id">
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
            <button
                class="button_for_slide_l"
                :disabled="pageNumber == 0"
                @click="prevPage"
            >
                Предыдущая страница
            </button>
            <button
                class="button_for_slide_r"
                :disabled="pageNumber >= pageCount - 1"
                @click="nextPage"
            >
                Следующая страница
            </button>
        </div>
        <div class="filters">
            <div class="filter_text">Поиск:</div>
            <input
                v-model="searchText"
                class="input_item_find"
                type="text"
            /><SearchSvg class="input_svg" />
            <div class="filter_text">Цена:</div>
            <div class="filter_text_price">От До</div>
            <div>
                <input
                    v-model.number="minPrice"
                    type="number"
                    class="input_item"
                /><SearchSvg class="input_svg" />
                <input
                    v-model.number="maxPrice"
                    type="number"
                    class="input_item"
                /><SearchSvg class="input_svg" />
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
    props: {
        size: {
            type: Number,
            required: false,
            default: 3,
        },
    },
    data() {
        return {
            maxPrice: 99999,
            minPrice: 0,
            searchText: '',
            sort: 'ascendingValue',
            instruments: false,
            pageNumber: 0,
        }
    },
    computed: {
        ...mapGetters('items', ['getItems']),
        ...mapGetters('cart', ['getCart']),
        orderedItems: function() {
            const { searchText } = this
            let c = this.items
            // eslint-disable-next-line prettier/prettier
            c = c.filter(p => p.value >= this.minPrice && p.value <= this.maxPrice)
            // eslint-disable-next-line prettier/prettier
            c = c.filter(p => p.name.toLowerCase().indexOf(searchText.toLowerCase()) !== -1)
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
            return this.getCart
        },
        items: function() {
            return this.getItems
        },
        pageCount() {
            let l = this.orderedItems.length,
                s = this.size
            return Math.ceil(l / s)
        },
        paginatedData() {
            const start = this.pageNumber * this.size,
                end = start + this.size
            return this.orderedItems.slice(start, end)
        },
    },
    methods: {
        ...mapMutations(['addToCart']),
        addToCart: function(itemId) {
            this.$store.commit('cart/addToCart', { id: itemId })
        },
        getLink: function(itemId) {
            return '/shop/item/' + itemId
        },
        nextPage() {
            this.pageNumber++
        },
        prevPage() {
            this.pageNumber--
        },
    },
}
</script>

<style lang="scss" scoped>
* {
    box-sizing: border-box;
}
.input {
    width: 60px;
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
                margin-left: 118px;
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
.filters {
    background: #ffffff;
    position: sticky;
    top: 0px;
    left: 1160px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
    margin: 0px 20px 20px 20px;
    padding: 18px 30px 82px 35px;
    .filter_text {
        align-items: center;
        margin-bottom: 5px;
        color: #545969;
        font-size: 24px;
    }
    .filter_text_price {
        word-spacing: 76px;
        margin-bottom: 5px;
    }
}
.input_svg {
    position: absolute;
    z-index: 1;
    top: 0;
    right: 0;
    width: 23px;
    &:hover {
        cursor: pointer;
    }
}
.input_item {
    margin: 0px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: black;
    border-radius: 1px;
    border-block-color: black;
    width: 100px;
    height: 33px;

    &:hover {
        cursor: pointer;
    }
    &:focus ~ .input__hint {
        opacity: 0;
        transition: 0.3s;
    }
}
.input_item_find {
    margin: 0px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: black;
    border-radius: 1px;
    border-block-color: black;
    width: 200px;
    height: 33px;
    margin-bottom: 10px;

    &:hover {
        cursor: pointer;
    }
    &:focus ~ .input__hint {
        opacity: 0;
        transition: 0.3s;
    }
}
.input_item_size {
    margin: 0px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 18px;
    color: #4c62b4;
    border-radius: 1px;
    border-block-color: black;
    width: 25px;
    height: 33px;
    margin-bottom: 10px;
    text-align: center;

    &:hover {
        cursor: pointer;
    }
    &:focus ~ .input__hint {
        opacity: 0;
        transition: 0.3s;
    }
}
input[type='number'] {
    -moz-appearance: textfield;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}
.span_class {
    margin-left: 280px;
}
.button_for_slide_r {
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    margin-top: 5px;
    margin-bottom: 5px;
    width: 200px;
    height: 30px;
    border-radius: 1.5px;
    border-block-color: black;
    background-color: beige;
}
.button_for_slide_l {
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    margin-top: 5px;
    margin-bottom: 5px;
    margin-right: 423px;
    width: 200px;
    height: 30px;
    border-radius: 1.5px;
    border-block-color: black;
    background-color: beige;
}
</style>
