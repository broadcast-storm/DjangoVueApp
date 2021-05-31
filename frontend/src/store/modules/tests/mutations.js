const mutations = {
    deleteTest(state, id) {
        state.tests.map(test =>
            test.id === id ? (test.status = 'passed') : test
        )
    },
}

export default mutations
