from fastapi import FastAPI
from routers import users,products,orders,carts,payments
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

router = FastAPI()

router.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router.include_router(users.router, prefix='/users')
router.include_router(products.router, prefix='/products')
router.include_router(carts.router, prefix='/carts')
router.include_router(orders.router, prefix='/orders')
router.include_router(payments.router,prefix='/payments' )

handler = Mangum(router, lifespan="off")