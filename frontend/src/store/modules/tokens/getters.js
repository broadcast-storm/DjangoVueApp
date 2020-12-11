const getters = {
    isAuthenticated: state => state.csrfToken !== null,
    getUserData: state => state.user,
}

export default getters
