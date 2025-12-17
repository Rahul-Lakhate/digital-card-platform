from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    slug = Column(String, unique=True)
    full_name = Column(String)
    title = Column(String)
    company = Column(String)
    phone = Column(String)
    template_id = Column(Integer)

