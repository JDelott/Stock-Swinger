import requests

# Replace 'YOUR_API_KEY' with your Alpha Vantage API key
api_key = "CD5ZF79XNSKBQU8A"

# Define the stock symbol you want to fetch data for
symbol = "LAC"  # Replace with your desired stock symbol

# Define the endpoint URL
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo"

# Send a GET request to the Alpha Vantage API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # The 'data' variable now contains the JSON response from the API
    # You can process and work with this data as needed
if response.status_code == 200:
    data = response.json()
    # Print the entire response data
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
