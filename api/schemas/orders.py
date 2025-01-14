from pydantic import BaseModel

class orderSchemas(BaseModel):
    total_amount:float
    cart_id:int
    order_ship_address:str
    shipping_fee:float
    receiver_phone:str