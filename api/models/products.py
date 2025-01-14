from .base import MyBaseModel
import peewee as p
from fastapi import UploadFile,HTTPException
from utils.product_util import FirebaseSto
class Products(MyBaseModel):
    name = p.TextField()
    quantity = p.IntegerField()
    price = p.FloatField()
    discount = p.FloatField()
    img_link = p.TextField()
    description = p.TextField()

    def uploadProduct(name:str,quantity:int,price:float, description:str,discount:int,image: UploadFile):
        try:
            fbStorage =  FirebaseSto()
            img_link = fbStorage.upload_image(image)
            new_product = Products.create( 
                name=name,
                price=price,
                quantity=quantity,
                description=description,
                discount=discount,
                img_link=img_link)
            return new_product
        except Exception as e:
            raise HTTPException(status_code=500, detail="Server error")
    
    def getAllProduct():
        try:
            product_list = Products.select().limit(20).dicts()
            return list(product_list)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Server error")
    
    def getProductById(id:int):
        try:
            product = Products.get_or_none(Products.id==id)
            if product:
                return product
            else:
                raise HTTPException(status_code=404, detail="Product Not Found")
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Server error")

    @classmethod   
    def to_dict(cls):
        return {
            "id":cls.id,
            "name": cls.name,
            "price": cls.price,
            "quantity": cls.quantity,
            "description": cls.description,
            "discount": cls.discount,
            "img_link":cls.img_link,
        }

