from sqlalchemy import Column, Integer, String

from app.db.base_class import Base



class Grant(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    ticket_label = Column(String(255), nullable=False)
    amount = Column(String(10), nullable=False)

