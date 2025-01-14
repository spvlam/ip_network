from fastapi import APIRouter,UploadFile,File,Form
from models.products import Products
from schemas.products import ProductsSchema
import json
router = APIRouter()


@router.post("/")
def uploadProduct(product_data: str = Form(...),image:UploadFile=File(...)):
    product_data_dict = json.loads(product_data)
    product = ProductsSchema(**product_data_dict)
    return Products.uploadProduct(product.name,product.quantity,product.price,product.description,product.discount,image)

@router.get("/")
def getAllProduct():
    return Products.getAllProduct()
@router.get("/{id}")
def getProductById(id:int):
    return Products.getProductById(id)