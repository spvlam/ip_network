import { MyResponseData, ResponseProductList, ResponseCartList } from "./types";
import { useAuthStorage } from "./authStore";
import { toast } from "vue3-toastify";
// const BASE_API_URL = import.meta.env.VITE_API_BASE_URL;
const BASE_API_URL = "http://localhost:8000/"


const fetchingData = async <ResponseData = null>(
    endpoint: string,
    optionsData?: RequestInit,
    extra?: {
        isAuth?: boolean;
    }
): Promise<MyResponseData<ResponseData>> => {
    const store = useAuthStorage();
    const res = await fetch(
        `${BASE_API_URL}${endpoint}`,
        extra?.isAuth
            ? {
                ...optionsData,
                headers: {
                    ...optionsData?.headers,
                    Authorization: `Bearer ${store.accessToken}`,
                    ...(store.refreshToken ? { 'X-Refresh-Token': store.refreshToken } : {})
                },
            }
            : optionsData
    );

    let data
    try {
        data = await res.json();
    } catch (err) {
        // Handle JSON parse error if needed
    }

    if (!res.ok) {
        return {
            isError: true,
            error: data?.detail || "An error on server",
            data: null
        };
    }
    return {
        isError: false,
        error: null,
        data: data as ResponseData
    };
};

export const RegisterUser = async (email: String,
    password: String,
    name: String) => {

    return fetchingData("users/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email, password }),
    })
}

export const login = async (email: String,
    password: String,is_admin:Boolean) => {

    return fetchingData("users/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password, is_admin }),
    })
}

export const getAllProduct = async () => {
    return fetchingData<ResponseProductList>("products", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
}

export const getProductDetail = async (id: number) => {
    return fetchingData<ResponseProductList>(`products/${id}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
}

export const addProductToCart = async (product_id: Number,
    user_id: Number,
    is_active: Boolean,
    quantity: Number) => {

    return fetchingData("carts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ product_id, user_id, is_active, quantity }),
    })
}

export const getCartDetail = async (id: number) => {
    return fetchingData<ResponseCartList>(`carts/${id}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
}

export const makePayment = async (total_amount: Number, cart_id: Number, order_ship_address: String, shipping_fee: Number, receiver_phone: String) => {
    const { isError, error, data } = await fetchingData('orders', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ total_amount, cart_id, order_ship_address, shipping_fee, receiver_phone })
    })

    if (isError) {
        toast.error(String(error))
    } else {
        const res = await fetchingData('payments', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ "order_id": data, "amount": total_amount })
        })
        if (res.isError) {
            toast.error(String(res.error))
        } else {
            window.open(String(res.data), '_blank');
        }

    }
}

export const getOrderDetail = async(id:Number)=>{
    const {isError,error, data} = await fetchingData('orders/'+id)
    if(!isError){
        return data
    }
}

export const getAllOrder = async () => {
    return fetchingData<ResponseProductList>("orders", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
        },
    })
}

export const uploadProduct = async(formData:any)=>{
    return await fetch("http://localhost:8000/products/",{
        method:"POST",
        headers: {
            'Accept': 'application/json',
        },
        body:formData
    })
}
