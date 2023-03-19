from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base


class DeliveryAddress(Base):
    id = Column(Integer, primary_key=True, index=True)
    locality = Column(String(255))
    route = Column(String(255))
    postal_code = Column(String(5))
    street_number = Column(String(255))
    apartment_number = Column(String(255))
    digicode = Column(String(255))
    phone = Column(String(255))
    additional_info = Column(String(255))
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=True)
