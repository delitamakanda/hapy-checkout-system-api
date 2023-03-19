from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


class Discount(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    value = Column(String(100), nullable=False)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=True)

