from passlib.context import CryptContext
import jwt
from typing import Dict
import os
from dotenv import load_dotenv

load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TIME_EXPIRE = os.getenv("ACCESS_TIME_EXPIRE")
REFRESH_TIME_EXPIRE = os.getenv("REFRESH_TIME_EXPIRE")
class UserUtil:
    def hashPassword(password: str) -> str:
        return pwd_context.hash(password)

    def verifyPassword(rawPass: str, hashedPass: str) -> bool:
        return pwd_context.verify(rawPass, hashedPass)

    @staticmethod
    def generateToken(email: str, is_admin: bool, token_type:bool) -> str:
        """
        token_type = true => access token
        """
        expiration = ACCESS_TIME_EXPIRE if token_type else REFRESH_TIME_EXPIRE
        payload = {
        "sub": email,        
        "is_admin": is_admin,            
        "exp":expiration 
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return token
    

    @staticmethod
    def verifyToken(token: str) -> Dict:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
