export const namespaced = false

export const state = {
    items: [
        {
            id: 1,
            img: require('@/assets/img/shop/item.png'),
            name: 'Название товара',
            description:
                '[Описание товара такое красивое, сил нет, сразу этот товар купить хочется]',
            value: 30000,
            level: 70,
        },
        {
            id: 2,
            img: require('@/assets/img/shop/item.png'),
            name: 'Название товара',
            description:
                '[Описание товара такое красивое, сил нет, сразу этот товар купить хочется]',
            value: 50000,
            level: 75,
        },
        {
            id: 3,
            img: require('@/assets/img/shop/item.png'),
            name: 'Название товара',
            description:
                '[Описание товара такое красивое, сил нет, сразу этот товар купить хочется]',
            value: 70000,
            level: 30,
        },
        {
            id: 4,
            img: require('@/assets/img/shop/item.png'),
            name: 'Название товара',
            description:
                '[Описание товара такое красивое, сил нет, сразу этот товар купить хочется]',
            value: 35000,
            level: 70,
        },
        {
            id: 5,
            img: require('@/assets/img/shop/item.png'),
            name: 'Название товара',
            description:
                '[Описание товара такое красивое, сил нет, сразу этот товар купить хочется]',
            value: 40000,
            level: 70,
        },
    ],
}

export const getters = {
    getItems: state => state.items,
}
