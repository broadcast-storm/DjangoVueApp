import Vue from 'vue'
import Vuex from 'vuex'

import * as auth from '@/store/modules/auth.js'
import * as tasks from '@/store/modules/tasks.js'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        auth,
        tasks
    }
})
