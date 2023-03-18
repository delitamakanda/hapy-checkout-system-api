from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.student import Student


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(20))
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    badge_number = Column(String(100))
    student = Column(ForeignKey("student.id"), nullable=True)
