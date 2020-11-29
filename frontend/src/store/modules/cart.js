export const namespaced = false

export const state = {
    cart: [],
    status: false,
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
    changeStatus(state) {
        state.status = true
    },
}
