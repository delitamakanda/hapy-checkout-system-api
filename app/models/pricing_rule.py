from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.db.base_class import Base



class PricingRule(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(100), unique=True, nullable=False)
    apply_scope = Column(JSON, nullable=False)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=True)
