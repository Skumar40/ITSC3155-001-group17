from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ReviewBase(BaseModel):
    customer_id: int
    sandwich_id: int
    rating: int = Field(ge=1, le=5)
    comment: str | None = Field(default=None, max_length=500)


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    customer_id: int | None = None
    sandwich_id: int | None = None
    rating: int | None = Field(default=None, ge=1, le=5)
    comment: str | None = Field(default=None, max_length=500)


class Review(ReviewBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    review_date: datetime
