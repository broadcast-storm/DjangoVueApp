import { AXIOS_YG_API } from '@/axiosConfig'

const actions = {
    getProfileData: async ({ commit }) => {
        try {
            AXIOS_YG_API.get('/api/tasks').then(data => {
                console.log(data)
                commit('SET_USER_TASKS', { data })
            })
        } catch (error) {
            console.log(error)
            throw error
        }
    },
}

export default actions
