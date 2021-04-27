import Vue from 'vue'
import Vuex from 'vuex'

import * as auth from '@/store/modules/auth.js'
import * as tasks from '@/store/modules/tasks.js'
import items from '@/store/modules/items'
import cart from '@/store/modules/cart'
import tests from '@/store/modules/tests'
import tokens from '@/store/modules/tokens'
import raiting from '@/store/modules/raiting'
import statistics from '@/store/modules/statistics'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth,
        tasks,
        items,
        cart,
        tokens,
        tests,
        raiting,
        statistics,
    },
})
