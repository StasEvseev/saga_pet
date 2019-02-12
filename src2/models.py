from database import Base
from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.types import DateTime


class Payment(Base):
    """
    Example Signups table
    """
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    date = Column(DateTime())
    amount = Column(DECIMAL)
