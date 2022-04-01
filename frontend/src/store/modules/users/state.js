const state = {
    isLoading: true,
    users: [
        {
            id: 1,
            img: require('@/mocks/woman.png'),
            name: 'Алина Пушкина',
            team: 'ВКЦ',
            productivity: '35',
            quality: '45',
            level: '65',
        },{
            id: 2,
            img: require('@/mocks/woman.png'),
            name: 'Катя Пушкина',
            team: 'ВКЦ',
            productivity: '65',
            quality: '35',
            level: '65',
        },{
            id: 3,
            img: require('@/mocks/woman.png'),
            name: 'Катя Тишкина',
            team: 'ВКЦ',
            productivity: '65',
            quality: '35',
            level: '65',
        }
    ],
}

export default state
