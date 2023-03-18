from sqlalchemy import Column, Integer, String

from app.db.base_class import Base



class Fee(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    tax_rate = Column(String(10), nullable=False)
    quantity = Column(Integer, nullable=False)
    amount = Column(String(10), nullable=False)

