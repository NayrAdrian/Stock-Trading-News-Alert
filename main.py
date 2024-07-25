import requests
from datetime import datetime, timedelta

stock_price_api_key = "C7B7CR0Z5UP9UKL4"
stock_price_end_point = "https://www.alphavantage.co/query"

news_api_key = "b58e8dba9f5d4bb0bb1c23a990101fd1"
news_end_point = "https://newsapi.org/v2/everything"

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
if abs(yesterday_close - day_before_yesterday_close) / day_before_yesterday_close >= 0.05:

    # Fetch the news data
    news_response = requests.get(news_end_point, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()

    # Print the title and description of the first 3 news articles
    articles = news_data.get("articles", [])
    for i, article in enumerate(articles[:3], start=1):
        print(f"Article {i}:")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}\n")


else:
    print(f"No significant changes in stock price from {day_before_yesterday} to {yesterday}")


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
