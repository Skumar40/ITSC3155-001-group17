from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class PromotionBase(BaseModel):
    code: str = Field(min_length=1, max_length=50)
    discount_percent: Decimal = Field(gt=0, le=100, max_digits=5, decimal_places=2)
    description: str | None = Field(default=None, max_length=300)


class PromotionCreate(PromotionBase):
    pass


class PromotionUpdate(BaseModel):
    code: str | None = Field(default=None, min_length=1, max_length=50)
    discount_percent: Decimal | None = Field(
        default=None, gt=0, le=100, max_digits=5, decimal_places=2
    )
    description: str | None = Field(default=None, max_length=300)


class Promotion(PromotionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
