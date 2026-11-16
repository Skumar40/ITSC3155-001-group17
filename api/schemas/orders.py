from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from .order_details import OrderDetail

class OrderBase(BaseModel):
    customer_name: str
    description: Optional[str] = None
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None


class Order(OrderBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
