import Vue from 'vue'
import Vuex from 'vuex'

import * as auth from '@/store/modules/auth.js'
import * as tasks from '@/store/modules/tasks.js'
import * as mainQuest from '@/store/modules/mainQuest.js'
import items from '@/store/modules/items'
import cart from '@/store/modules/cart'
import tests from '@/store/modules/tests'
import tokens from '@/store/modules/tokens'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth,
        tasks,
        items,
        cart,
        tokens,
        tests,
        mainQuest,
    },
})
