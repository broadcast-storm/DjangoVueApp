import Vue from 'vue'
import Vuex from 'vuex'

import * as auth from '@/store/modules/auth.js'
import * as mainQuest from '@/store/modules/mainQuest.js'
import profile from '@/store/modules/profile'
import items from '@/store/modules/items'
import cart from '@/store/modules/cart'
import tests from '@/store/modules/tests'
import tokens from '@/store/modules/tokens'
import rating from '@/store/modules/rating'
import statistics from '@/store/modules/statistics'
import tasks from '@/store/modules/tasks'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        profile,
        auth,
        items,
        cart,
        tokens,
        tests,
        mainQuest,
        rating,
        statistics,
        tasks,
    },
})
