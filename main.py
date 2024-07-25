import requests
from datetime import datetime, timedelta

stock_price_api_key = "C7B7CR0Z5UP9UKL4"
stock_price_end_point = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_price_api_key,
}

# Fetch the stock price data
stock_price_response = requests.get(stock_price_end_point, params=stock_price_params)
stock_price_response.raise_for_status()
stock_price_data = stock_price_response.json()

# Get the time series data
time_series = stock_price_data["Time Series (Daily)"]

# Get dates for yesterday and the day before yesterday
yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
day_before_yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')

# Get closing prices for the specified dates
yesterday_close = float(time_series[yesterday]["4. close"])
day_before_yesterday_close = float(time_series[day_before_yesterday]["4. close"])

# Print closing prices
print(f"{yesterday}: {COMPANY_NAME} [{STOCK}] closing price: {yesterday_close}")
print(f"{day_before_yesterday}: {COMPANY_NAME} [{STOCK}] closing price: {day_before_yesterday_close}")

# Check for a 5% change and print "Get News" if condition is met
if abs(yesterday_close - day_before_yesterday_close) / day_before_yesterday_close >= 0.05:
    print("Get News")

#  STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#  STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
