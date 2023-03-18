from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Address(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    lat = Column(String(255))
    lng = Column(String(255))
    timezone_id = Column(String)
    locality = Column(String(255))
    route = Column(String(255))
    postal_code = Column(String(5))
    street_number = Column(String(255))
    administrative_area_level_1 = Column(String(255))
    administrative_area_level_2 = Column(String(255))
    country = Column(String(255))
    google_place_id = Column(String(255))
    phone = Column(String(255))
