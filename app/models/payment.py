from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class Payment(Base):
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255), nullable=False)
    amount = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)

