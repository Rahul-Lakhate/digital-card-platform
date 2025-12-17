from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    razorpay_order_id = Column(String)
    razorpay_payment_id = Column(String)
    status = Column(String)

