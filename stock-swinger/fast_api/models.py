# models.py

from sqlalchemy import Column, Integer, String, JSON
from .database import Base


class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    data = Column(JSON)
