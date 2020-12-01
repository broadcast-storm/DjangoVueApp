const mutations = {
    addToCart(state, itemId) {
        state.cart.push(itemId)
    },
    clearCart(state) {
        state.cart = []
    },
}

export default mutations
