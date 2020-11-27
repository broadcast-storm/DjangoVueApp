const getters = {
    isAuthenticated: state => state.csrfToken !== null,
}

export default getters
