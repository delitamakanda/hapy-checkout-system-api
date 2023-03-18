from sqlalchemy import Column, Integer, String

from app.db.base_class import Base



class LoyaltyPrograms(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    amount = Column(String(10), nullable=False)
