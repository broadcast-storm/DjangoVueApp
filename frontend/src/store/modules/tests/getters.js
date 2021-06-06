const getters = {
    getTests: state => state.tests,
    getTestsList: state => ({
        status: state.testsStatus,
        data: state.testsList,
    }),
    getQuestionsList: state => ({
        status: state.questionsStatus,
        data: state.questionsList,
    }),
}

export default getters
