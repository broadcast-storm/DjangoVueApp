import Vue from 'vue'
import Vuex from 'vuex'

import * as auth from '@/store/modules/auth.js'
import * as tasks from '@/store/modules/tasks.js'
import * as items from '@/store/modules/items.js'
import * as cart from '@/store/modules/cart.js'
import tokens from '@/store/modules/tokens'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth,
        tasks,
        items,
        cart,
        tokens,
    },
})
