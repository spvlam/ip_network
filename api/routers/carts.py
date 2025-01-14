from fastapi import APIRouter,Response
from models.carts import Carts
from schemas.carts import CartAddSchema
router = APIRouter()

@router.post("/")
def cartAddProduct(requestCart:CartAddSchema,response:Response):
    return Carts.cartAddProduct(requestCart.product_id,requestCart.user_id, requestCart.is_active ,requestCart.quantity,response)

@router.get("/{cart_id}")
def cartGetDetail(cart_id:int):
    return Carts.getCurrentCart(cart_id)