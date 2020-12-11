import Vue from 'vue'
import Vuex from 'vuex'

import items from '@/store/modules/items'
import cart from '@/store/modules/cart'
import tokens from '@/store/modules/tokens'
import profile from '@/store/modules/profile'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        items,
        cart,
        tokens,
        profile,
    },
})
