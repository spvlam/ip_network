
import peewee as p
from peewee import DoesNotExist
from .base import MyBaseModel
from utils.user_utils import UserUtil
from fastapi import HTTPException,Response

class Users(MyBaseModel):
    name = p.TextField()
    password = p.TextField()
    email = p.TextField()
    role = p.BooleanField()

    def register(email :str,password:str,name:str,response:Response):
        hashPass = UserUtil.hashPassword(password)
        try:
            try:
                checkUser = Users.get(Users.email == email)
                print(checkUser)
                raise HTTPException(status_code=409, detail="User already exists")
            except DoesNotExist:
                new_user = Users.create(
                    name=name,
                    password=hashPass,
                    email=email,
                    role=False
                )
                response.status_code=200
                return {"message":"create user successfully"}
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Server error")
    
    def login(email:str,password:str,is_admin:bool,response:Response):
        try:
            checkUser = Users.get(Users.email == email)
            if  UserUtil.verifyPassword(password,checkUser.password):
                if(is_admin != checkUser.role):
                    raise HTTPException(status_code=401, detail="Wrong role") 
                access_token = UserUtil.generateToken(email,is_admin,True)
                refresh_token = UserUtil.generateToken(email,is_admin,False)
                response_data = {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "name": checkUser.name,
                "id": checkUser.id
                
            }
                response.status_code=200
                return response_data
            else:
                raise HTTPException(status_code=401, detail="Wrong Password")
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="User Not Found")
       

        
        


