// the union of more type, in this case we have success and failure type
export type MyResponseData<T> =
    | {
        isError: true,
        error: String,
        data?: null
    }
    | {
        isError: false,
        error?: null,
        data: T
    }

type BaseProduct = {
    id: number,
    name: string,
    quantity: number,
    price: number,
    img_link: string,
}

export type ResponseProduct = BaseProduct & {
    discount: number,
}

export type CartDetail = BaseProduct & {
    product_id: number,
    description: number,
}
export type ResponseCartList = {
    items: CartDetail[]
}

export type ResponseProductList = {
    items: ResponseProduct[]
}
