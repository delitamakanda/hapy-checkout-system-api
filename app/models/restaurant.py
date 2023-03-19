from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.address import Address


class Restaurant(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(ForeignKey("restaurant.id"), nullable=False)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=True)
