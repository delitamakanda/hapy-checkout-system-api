from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.base_class import Base



class Tag(Base):
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String(100), unique=True, nullable=False)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=True)

