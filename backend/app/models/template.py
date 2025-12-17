from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    name = Column(String)

