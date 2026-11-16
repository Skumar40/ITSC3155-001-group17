from sqlalchemy import CheckConstraint, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5", name="ck_reviews_rating"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), index=True, nullable=False)
    sandwich_id = Column(Integer, ForeignKey("sandwiches.id"), index=True, nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500))
    review_date = Column(DateTime, nullable=False, server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    sandwich = relationship("Sandwich", back_populates="reviews")
