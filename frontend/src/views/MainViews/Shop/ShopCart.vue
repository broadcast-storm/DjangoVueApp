<template>
    <div class="cart-wrapper">
        <div v-if="cart.length == 0" class="cart__cleared">
            <div class="cart__header">
                <router-link to="/shop" class="cart__back"
                    >Вернуться к покупкам</router-link
                >
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
                <router-link to="/shop" class="cart__back"
                    >Вернуться к покупкам</router-link
                >
                <h2 class="cart__headline">Корзина</h2>
            </div>
            <div v-for="item in items" :key="item.id" class="shop__item">
                <div class="shop__item-img">
                    <img :src="item.img" alt="" />
                </div>
                <div class="shop__item-description">
                    <h3 class="item-headline">{{ item.name }}</h3>
                    <span class="item-description">{{ item.description }}</span>
                    <span class="item-value"
                        >{{ item.value }}<CoinSvg class="item-icon"
                    /></span>
                    <span class="item-required_level"
                        >требуемый уровень: {{ item.level }}</span
                    >
                </div>
            </div>
        </div>
        <div v-if="cart.length != 0" class="cart__state">
            <div class="cart__state-card">
                <h3 class="card-headline">В корзине</h3>
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
                    купить<Arrow class="arrow" />
                </button>
            </div>
            <button class="cart__clear" @click="clearCar()">
                Очистить корзину
            </button>
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
            let items = this.getItems
            let cart = this.getCart
            return items.filter(a => cart.filter(b => b.id == a.id).length != 0)
        },
        cart: function() {
            return this.getCart
        },
        cartSumm: function() {
            let summ = 0
            for (let i of this.items) {
                summ += i.value
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
* {
    box-sizing: border-box;
}
.cart-wrapper {
    display: flex;
    flex-direction: row;
    margin-top: 90px;
    width: 100%;
}
.cart__cleared {
    height: calc(100vh - 90px);
    width: 100%;
    .cart__header {
        margin-left: 27px;
    }
    &-status {
        // width: 100vh;
        display: flex;
        align-items: center;
        flex-direction: column;
        margin-top: 242px;
        .items-bought {
            font-size: 48px;
            line-height: 28px;
            color: #1a2740;
            margin-bottom: 35px;
        }
        .items-information {
            font-size: 36px;
            line-height: 28px;
            color: #545969;
        }
    }
}
.cart__header {
    margin-top: 16px;
    margin-left: -35px;
    margin-bottom: 45px;
    z-index: 9999;
    .cart__back {
        font-size: 28px;
        line-height: 28px;
        color: #535a70;
    }
    .cart__headline {
        font-size: 48px;
        line-height: 28px;
        color: #1a2740;
        margin-top: 16px;
    }
}
.cart__list {
    height: calc(100vh - 90px);
    overflow-y: scroll;
    padding-left: 62px;
    .shop__item {
        margin-top: 22px;
        margin-right: 35px;
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
                padding-bottom: 40px;
                .item-icon {
                    height: 34px;
                    width: 34px;
                    padding-left: 5px;
                }
            }
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
                background: #5F66A9;
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

.cart__state {
    margin-top: 142px;
    margin-left: 42px;
    &-card {
        background: #ffffff;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        width: 311px;
        height: 245px;
        margin-bottom: 40px;
        padding-left: 40px;
        padding-right: 42px;
        padding-top: 25px;
        padding-bottom: 26px;
        display: flex;
        flex-direction: column;
        .card {
            &-headline {
                font-size: 28px;
                line-height: 28px;
                color: #1a2740;
            }
            &-number {
                font-size: 24px;
                line-height: 28px;
                color: #7d849a;
                margin-bottom: 22px;
            }
            &-value {
                display: flex;
                align-items: center;
                font-size: 48px;
                line-height: 28px;
                color: #1a2740;
                margin-bottom: 47px;
                .item-icon {
                    height: 37px;
                    width: 50px;
                    padding-left: 11px;
                }
            }
            &-buy {
                background: #5F66A9;
                height: 36px;
                width: 174px;
                box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
                border-radius: 5px;
                font-size: 24px;
                line-height: 16px;
                color: #fff;
                border: none;
                outline: none;
                align-self: flex-end;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding-left: 21px;
                padding-right: 13.5px;
                cursor: pointer;
                .arrow {
                    height: 12px;
                    width: 7.41px;
                }
            }
        }
    }
    .cart__clear {
        width: 310px;
        height: 36px;
        font-size: 24px;
        line-height: 28px;
        color: #fff;
        background: #7d849a;
        box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
        border-radius: 5px;
        border: none;
        outline: none;
        cursor: pointer;
    }
}
</style>
