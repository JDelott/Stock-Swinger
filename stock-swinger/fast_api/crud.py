from sqlalchemy.orm import Session
from .models import StockData


def create_stock_data(db: Session, symbol: str, data: dict):
    db_stock_data = StockData(symbol=symbol, data=data)
    db.add(db_stock_data)
    db.commit()
    db.refresh(db_stock_data)
