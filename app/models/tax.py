from sqlalchemy import Column, Integer, String

from app.db.base_class import Base



class Tax(Base):
    id = Column(Integer, primary_key=True, index=True)
    tax_rate = Column(String(10), nullable=False)
    total_tax = Column(String(10), nullable=False)
    total_price_discounted_with_tax_included = Column(String(10), nullable=False)
    total_excl_tax = Column(String(10), nullable=False)
