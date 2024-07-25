import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

# Retrieve the API keys and tokens from environment variables
stock_price_api_key = os.getenv("STOCK_PRICE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

stock_price_end_point = "https://www.alphavantage.co/query"  # Alpha Vantage
news_end_point = "https://newsapi.org/v2/everything"  # News API

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_COMPANY_NAME = "tesla"

# Parameters for the stock price API request
stock_price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_price_api_key,
}

# Parameters for the news API request
news_params = {
    "q": NEWS_COMPANY_NAME,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 5,  # Fetch the first 3 news articles
    "apiKey": news_api_key,
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
percentage_change = (yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100
if abs(percentage_change) >= 5:

    # Fetch the news data
    news_response = requests.get(news_end_point, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    # Print the title and description of the first 3 news articles
    articles = news_data.get("articles", [])
    message_body = f"{COMPANY_NAME} [{STOCK}]: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change):.2f}%\n"
    for i, article in enumerate(articles[:3], start=1):
        message_body += f"\nArticle {i}:\n\n"
        message_body += f"Headline: {article['title']}\n\n"
        message_body += f"Brief Summary: {article['description']}\n\n"
        message_body += f"Source: {article['source']['name']}\n"

    # Send message via Twilio
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='whatsapp:+123456',  # Enter From Number here
            body=message_body,
            to='whatsapp:+123456'  # Enter To Number here
        )
        print(f"Message status: {message.status}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

else:
    print(f"No significant changes in stock price from {day_before_yesterday} to {yesterday}")