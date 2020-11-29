import { getCookie } from '@/utils/cookies'

const state = {
    accessToken: null,
    csrfToken: getCookie('csrftoken'),
    tokenStatus: '',
    firstRequestSuccess: false,
}

export default state
