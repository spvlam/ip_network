from .base import MyBaseModel
import peewee as p
from fastapi import HTTPException,Response
from .products import Products

class Carts(MyBaseModel):
    id = p.IntegerField()
    user_id = p.IntegerField()
    quantity = p.IntegerField()
    product_id = p.IntegerField()
    class Meta:
        primary_key = p.CompositeKey('id', 'product_id')

    def cartAddProduct(product_id:int,user_id:int,is_active:bool,quantity:int,response:Response):
        """
        is_active = false if cart has been existed
        """
        try:
            if is_active:
                Carts.update(is_active=False).where(Carts.user_id==user_id).execute()
                Carts.create(
                    user_id=user_id,
                    quantity=quantity,
                    product_id=product_id,
                    is_active=is_active
                )
                createdCart = Carts.select().where(Carts.user_id == user_id, Carts.is_active == is_active).first()
                return createdCart.id
            else:
                search_cart = Carts.get_or_none(is_active=True,user_id=user_id)
                if search_cart:
                    search_cart_pro = Carts.get_or_none(is_active=True,user_id=user_id,product_id=product_id)
                    if search_cart_pro:
                        search_cart_pro.quantity += quantity
                        search_cart_pro.save()
                    else :
                        Carts.create(
                        id=search_cart.id,
                        user_id=user_id,
                        quantity=quantity,
                        product_id=product_id,
                        is_active=True
                        )
                response.status_code =200
                return search_cart.id
        except HTTPException as e:
            raise HTTPException(status_code=500)
        
    def getCurrentCart(cart_id:int):
        try:
            query = (Carts
                .select(Carts, Products)
                .join(Products, on=(Carts.product_id == Products.id))
                .where(Carts.id == cart_id))
            result = list(query.dicts().execute())
            return result
        except HTTPException as e:
            raise HTTPException(status_code=500)
        
    


            


        