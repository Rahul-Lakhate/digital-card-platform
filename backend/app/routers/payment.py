from fastapi import APIRouter
import razorpay
from app.core.config import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET

router = APIRouter()
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@router.post("/create-order")
def create_order():
    order = client.order.create({
        "amount": 49900,
        "currency": "INR",
        "payment_capture": 1
    })
    return order

