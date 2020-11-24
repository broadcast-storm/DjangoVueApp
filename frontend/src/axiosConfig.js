import axios from 'axios'

const token = localStorage.getItem('accessToken')
if (token) {
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
}

export const AXIOS_YG_API = axios.create({
    baseURL: process.env.API_BASE_URL,
    timeout: 1000,
})
