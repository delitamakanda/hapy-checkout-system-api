import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String(255), index=True)
    student_number = Column(String(255))
    grade = Column(String(255))
    section = Column(String(255))
    sub_section = Column(String(255))
    grant_code = Column(String(255))
    entrance_fee_code = Column(String(255))
    tariff_code = Column(String(255))
    bar_code = Column(String(255))
    pricing_rule_code = Column(String(255))
    customer_id = Column(String(255))
    account_payment_method_type = Column(String(255))
    account_type = Column(String(255))
    access_from = Column(String(255))
    access_until = Column(DateTime(), default=datetime.datetime.now())
