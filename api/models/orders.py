from .base import MyBaseModel
import peewee as p
from peewee import DoesNotExist
from fastapi import HTTPException
from .carts import Carts
from .users import Users
from .payments import Payments
class Orders(MyBaseModel):
    cart_id = p.IntegerField()
    total_amount = p.FloatField()
    receiver_phone= p.TextField()
    order_ship_address = p.TextField()
    shipping_fee =  p.FloatField()

    def createOrder(total_amount:float,cart_id:int, order_ship_address :str,receiver_phone:str,shipping_fee:float):
        try:
            newOrder = Orders.create(
                cart_id = cart_id,
                total_amount =total_amount,
                receiver_phone= receiver_phone,
                order_ship_address = order_ship_address,
                shipping_fee = shipping_fee
            )
            Carts.update(is_active=False).where(Carts.id == cart_id).execute()
            return newOrder.id
        except Exception as e:
            raise HTTPException(status_code=500, detail="Server error")
    
    @classmethod
    def getAllOrder(cls):
        try:
            query = (cls
                .select(cls.id, 
                        cls.created_at, 
                        Users.name, 
                        cls.total_amount, 
                        Payments.result, 
                        cls.receiver_phone)
                .join(Carts, on=(cls.cart_id == Carts.id))
                .join(Users, on=(Carts.user_id == Users.id))
                .join(Payments, p.JOIN.LEFT_OUTER, on=(Payments.order_id == cls.id))
                )
            result = query.dicts().execute()
            # result is iterator => without converting , only get each element
            return list(result)
        except Exception as e:
            raise HTTPException(status_code=500, detail=e)
    
    def getOrderById(id:int):
        try:
            orderPay = Orders.get_by_id(id)
            return orderPay.__data__
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Order Not Found")

    