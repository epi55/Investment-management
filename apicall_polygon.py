import requests

api_key = 'YOUR_API_KEY'

ticker_symbol = 'AAPL'

# Define the endpoint URL
url = f'https://api.polygon.io/v2/aggs/ticker/{ticker_symbol}/range/1/day/20230101/20231020?unadjusted=true&apiKey={api_key}'

try:
    # Send a GET request to Polygon.io
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        print(f"Today's stock data for {ticker_symbol}:")
        print(data)
    else:
        print(f"Request failed with status code {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")