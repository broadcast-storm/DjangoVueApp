export const namespaced = false

export const state = {
    cart: [],
}

export const getters = {
    getCart: state => state.cart,
    getCartStatus: state => state.status,
}

export const mutations = {
    addToCart(state, itemId) {
        state.cart.push(itemId)
    },
    clearCart(state) {
        state.cart = []
    },
}
