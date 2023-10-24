# from fastapi import APIRouter, Query
# import requests

# stock_router = APIRouter()


# @stock_router.get("/get_stock_data/")
# async def get_stock_data(
#     symbol: str = Query(
#         ..., title="Stock Symbol", description="The stock symbol to fetch data for"
#     )
# ):
#     # Replace 'YOUR_API_KEY' with your Alpha Vantage API key
#     api_key = "CD5ZF79XNSKBQU8A"

#     # Define the endpoint URL
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&extended_hours=false&outputsize=compact&apikey={api_key}"

#     # Send a GET request to the Alpha Vantage API
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         return data  # This will return the JSON response to the client
#     else:
#         return {
#             "error": f"Failed to retrieve data. Status code: {response.status_code}"
#         }
# routers.py

from fastapi import APIRouter, Query
import requests
from sqlalchemy.orm import Session
from .database import database
from .models import StockData
from .crud import create_stock_data

stock_router = APIRouter()


@stock_router.get("/get_stock_data/")
async def get_stock_data(
    symbol: str = Query(
        ..., title="Stock Symbol", description="The stock symbol to fetch data for"
    )
):
    # Replace 'YOUR_API_KEY' with your Alpha Vantage API key
    api_key = "CD5ZF79XNSKBQU8A"

    # Define the endpoint URL
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&extended_hours=false&outputsize=compact&apikey={api_key}"

    # Send a GET request to the Alpha Vantage API
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Insert the data into the database
        create_stock_data(database, symbol, data)

        return data  # This will return the JSON response to the client
    else:
        return {
            "error": f"Failed to retrieve data. Status code: {response.status_code}"
        }
