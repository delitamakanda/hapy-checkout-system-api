from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship

from app.db.base_class import Base



class PricingRule(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), unique=True, nullable=False)
    apply_scope = Column(JSON, nullable=False)
    channels = relationship("Channel", back_populates="pricing_rule", cascade="all, delete-orphan", uselist=True)
