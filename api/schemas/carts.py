
from pydantic import BaseModel
class CartAddSchema(BaseModel):
    product_id:int
    user_id:int
    is_active:bool
    quantity:int