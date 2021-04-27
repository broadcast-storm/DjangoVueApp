const state = {
    accessToken: null,
    refreshToken: localStorage.getItem('refresh_token'),
    tokenStatus: '',
    firstRequestSuccess: false,
}

export default state
