from sqlalchemy import CheckConstraint, Column, Integer, Numeric, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Promotion(Base):
    __tablename__ = "promotions"
    __table_args__ = (
        CheckConstraint(
            "discount_percent > 0 AND discount_percent <= 100",
            name="ck_promotions_discount_percent",
        ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50), unique=True, nullable=False)
    discount_percent = Column(Numeric(5, 2), nullable=False)
    description = Column(String(300))

    orders = relationship("Order", back_populates="promotion")
