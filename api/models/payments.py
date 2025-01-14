from .base import MyBaseModel
import  peewee  as p 
from sub_system import vn_pay
from fastapi import Request,HTTPException,Response
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv
load_dotenv()
RETURN_RESULT_PAYMENT = os.getenv("RETURN_RESULT_PAYMENT")
class Payments(MyBaseModel):
    order_id = p.IntegerField()
    result = p.TextField()

    def makePaymentUrl(request:Request,order_id,amount):  
        return vn_pay.payment(request,str(order_id),int(amount))
    
    def savePaymentResult(vnp_ResponseCode:str,vnp_TransactionNo:str,vnp_TxnRef:str,response:Response):
        try:
            result = vn_pay.convertResult(vnp_ResponseCode)
            Payments.create(
                id=vnp_TransactionNo,
                order_id=vnp_TxnRef,
                result=result
            )
            response.status_code=200
            returnUrl = RETURN_RESULT_PAYMENT
            returnUrl = returnUrl + "?order_id=" + vnp_TxnRef +"&result="+result
            return RedirectResponse(url=returnUrl)
            # return {"result":result,"order_id":vnp_TxnRef}
        except HTTPException as e:
            Payments.create(
                id=vnp_TransactionNo,
                order_id=vnp_TxnRef,
                result="error insert DB"
            )
            raise HTTPException(status_code=500)

    