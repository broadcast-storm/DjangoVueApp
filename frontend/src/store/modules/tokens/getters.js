const getters = {
    isAuthenticated: state => state.refreshToken !== null,
}

export default getters
