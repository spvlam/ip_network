from fastapi import APIRouter
from models.orders import Orders
from schemas.orders import orderSchemas
router = APIRouter()


@router.post("/")
def createOrder(order_info:orderSchemas):
    return Orders.createOrder(order_info.total_amount,order_info.cart_id, order_info.order_ship_address ,order_info.receiver_phone,order_info.shipping_fee)

@router.get("/{id}")
def getOrderById(id:int):
    return Orders.getOrderById(id)

@router.get("/")
def getAllOrder():
    return Orders.getAllOrder()


