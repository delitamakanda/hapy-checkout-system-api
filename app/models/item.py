from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum

from app.db.base_class import Base

from app.models.tag import Tag
from app.models.category import Category

class StatusEnum(enum.Enum):
    PAID = 'paid'
    CANCELLED = 'cancelled'
    VALIDATED = 'validated'

class ItemType(enum.Enum):
    PRODUCT = 'product'
    CUSTOMIZATION = 'customization'

class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String(256), index=True)
    parent_item_id = Column(String(256), nullable=True)
    sku_value = Column(String(256), nullable=False)
    name = Column(String(256), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price_with_tax_included = Column(String(10), nullable=False)
    tax_rate = Column(String(10), nullable=False)
    free = Column(Boolean, default=False, nullable=False)
    status = Column(Enum(StatusEnum), nullable=False)
    item_type = Column(Enum(ItemType), nullable=False)
    discounted = Column(Boolean, default=False, nullable=False)
    reduced = Column(Boolean, default=False, nullable=False)
    service = Column(String)
    total_price_discounted = Column(String(10), nullable=False)
    total_item_discounted = Column(String(10), nullable=False)
    cancel_reason = Column(String(256), nullable=True)
    device_name = Column(String(256), nullable=True)
    device_id = Column(String(256), nullable=True)
    categories = Column(ForeignKey("category.id"), nullable=True)
    tags = Column(ForeignKey("tag.id"), nullable=True)

