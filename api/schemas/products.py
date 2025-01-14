from pydantic import BaseModel

class ProductsSchema(BaseModel):
    name:str
    quantity:int
    price:float
    description:str
    discount:int


