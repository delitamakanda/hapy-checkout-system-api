from sqlalchemy import Column, Integer, String

from app.db.base_class import Base



class EntranceFee(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), nullable=False)
    type = Column(String(100), nullable=False)
    ticket_label = Column(String(100), nullable=False)
    tax_rate = Column(String(10), nullable=False)
    amount = Column(String(10), nullable=False)

