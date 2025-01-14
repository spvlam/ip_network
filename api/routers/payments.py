from fastapi import APIRouter,Request,Response
from models.payments import Payments
from schemas.payments import PaymentSchema
router = APIRouter()

@router.post("/")
def makePaymentUrl(request:Request,paymentRequest:PaymentSchema):
    return Payments.makePaymentUrl(request,paymentRequest.order_id,paymentRequest.amount)

@router.get("/payment_return")
def getPayment(request:Request,response:Response):
    print(request)
    vnp_txn_ref = request.query_params.get('vnp_TxnRef')
    vnp_response_code = request.query_params.get('vnp_ResponseCode')
    vnp_transaction_no = request.query_params.get('vnp_TransactionNo')
    return Payments.savePaymentResult(vnp_response_code,vnp_transaction_no,vnp_txn_ref,response)