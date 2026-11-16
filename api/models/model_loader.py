from . import (
    customers,
    order_details,
    orders,
    payments,
    promotions,
    recipes,
    resources,
    reviews,
    sandwiches,
)
from ..dependencies.database import Base, engine


def index():
    Base.metadata.create_all(engine)
