from fastapi import APIRouter,Response
from models.users import Users
from schemas import users
router = APIRouter()


@router.post("/register")
def createUser(register_data:users.userRegister,response:Response):
    return Users.register(register_data.email,register_data.password,register_data.name,response)

@router.post("/login")
def createUser(login_data:users.userLogin,response:Response):
    return Users.login(login_data.email,login_data.password,login_data.is_admin,response)
