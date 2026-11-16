from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class PaymentBase(BaseModel):
    order_id: int
    amount: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    payment_method: str = Field(min_length=1, max_length=50)


class PaymentCreate(PaymentBase):
    pass


class PaymentUpdate(BaseModel):
    order_id: int | None = None
    amount: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    payment_method: str | None = Field(default=None, min_length=1, max_length=50)


class Payment(PaymentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    payment_date: datetime
