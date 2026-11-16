from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(254), unique=True, nullable=False)

    orders = relationship("Order", back_populates="customer")
    reviews = relationship("Review", back_populates="customer")
