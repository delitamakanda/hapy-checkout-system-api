from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from app.models.channel import Channel


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String(255), nullable=False, index=True, unique=True)
    is_superuser = Column(Boolean, default=False)
    channels = relationship("Channel", back_populates="submitter", cascade="all, delete-orphan", uselist=True)

