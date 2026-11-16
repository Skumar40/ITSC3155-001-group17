from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100))
    customer_id = Column(
        Integer, ForeignKey("customers.id", name="fk_orders_customer"), index=True
    )
    promotion_id = Column(
        Integer, ForeignKey("promotions.id", name="fk_orders_promotion"), index=True
    )
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")
    payments = relationship("Payment", back_populates="order")
