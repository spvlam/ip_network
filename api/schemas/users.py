from pydantic import BaseModel

class userBase(BaseModel):
    email:str
    password:str
class userLogin(userBase):
    is_admin:bool

class userRegister(userBase):
    name:str