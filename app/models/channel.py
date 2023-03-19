from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean, Enum
import enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base

from app.models.discount import Discount
from app.models.payment import Payment
from app.models.entrance_fee import EntranceFee
from app.models.fee import Fee
from app.models.grant import Grant
from app.models.pricing_rule import PricingRule
from app.models.customer import Customer
from app.models.item import Item
from app.models.tag import Tag
from app.models.tax import Tax
from app.models.restaurant import Restaurant
from app.models.delivery_address import DeliveryAddress

class ConsumptionMode(enum.Enum):
    MODE_DELIVERY = 1
    MODE_TAKE_AWAY = 2
    MODE_SIT_IN = 3
    MODE_DRIVE = 4

class ChannelEnum(enum.Enum):
    KIOSK = 1
    WEB = 2
    POS = 5

class statusEnum(enum.Enum):
    VALIDATED = 'validated'
    PAID = 'paid'
    CANCELLED = 'cancelled'

class webPaymentStatusEnum(enum.Enum):
    PAYMENT_PENDING = 'pending'
    PAYMENT_OK = 'ok'
    PAYMENT_REFUSED = 'refused'
    PAYMENT_REFUNDED = 'refunded'

class Channel(Base):
    id = Column(Integer, primary_key=True, index=True)
    channel_order_id = Column(String(256), nullable=False)
    brand_id = Column(String(256), nullable=False)
    consumption_mode_id = Column(Enum(ConsumptionMode), nullable=False)
    currency = Column(String, default='EUR', nullable=False)
    customer_id = Column(String(256), nullable=False)
    daily_order_id = Column(String(256), nullable=False)
    device_id = Column(String(256), nullable=False)
    device_name = Column(String(256), nullable=False)
    discounts = relationship("Discount", backref="channel")
    entrance_fees = relationship("EntranceFee", backref="channel")
    fees = relationship("Fee", backref="channel")
    grants = relationship("Grant", backref="channel")
    pricing_rule = relationship("PricingRule", backref="channel")
    items = relationship("Item", backref="channel")
    number_of_guests = Column(Integer, nullable=False)
    payments = relationship("Payment", backref="channel")
    restaurant_id = relationship("Restaurant", backref="channel")
    external_id = Column(String(256), nullable=True)
    seller = Column(String(256), default="Cashier", nullable=False)
    channel_id = Column(Enum(ChannelEnum), nullable=False)
    start_date = Column(DateTime, nullable=False)
    expected_date = Column(DateTime, nullable=False)
    business_year = Column(String(6), nullable=False)
    business_month = Column(String(6), nullable=False)
    business_day = Column(String(6), nullable=False)
    last_update_date = Column(DateTime, nullable=False)
    status = Column(Enum(statusEnum), default=statusEnum.VALIDATED, nullable=False)
    web_payment_status = Column(Enum(webPaymentStatusEnum), default=webPaymentStatusEnum.PAYMENT_PENDING, nullable=False)
    tags = relationship("Tag", backref="channel")
    taxes = relationship("Tax", backref="channel")
    total_price_discounted_with_tax_excluded = Column(String(10), nullable=False)
    total_amount_free = Column(String(10), nullable=False)
    total_item_free = Column(String(10), nullable=False)
    total_price_discounted_with_tax_included = Column(String(10), nullable=False)
    total_discount = Column(String(10), nullable=False)
    total_tax = Column(String(10), nullable=False)
    turnover = Column(String(10), nullable=True)
    marketplace_store_name = Column(String(256), nullable=True)
    service = Column(String(256), nullable=True)
    discount_employee_name = Column(String(256), nullable=True)
    discount_code = Column(String(256), nullable=True)
    cancellation_reason = Column(String(256), nullable=True)
    cancellation_reason_description = Column(String(256), nullable=True)
    total_amount_cancelled = Column(String(10), nullable=False)
    total_item_cancelled = Column(String(10), nullable=False)
    table_name = Column(String(256), nullable=True)
    ticket_number = Column(String(256), nullable=True)
    comment = Column(String(256), nullable=True)
    is_cancellable = Column(Boolean, default=True, nullable=False)
    is_refundable = Column(Boolean, default=True, nullable=False)
    customer = relationship("Customer", backref="channel")
    delivery_address = relationship("DeliveryAddress", backref="channel")
    submitter_id = Column(String(10), ForeignKey("user.id"), nullable=True)
    submitter = relationship("User", back_populates="channels")

