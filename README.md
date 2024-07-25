**Stock Price Alert and News Fetcher**

This Python program monitors the closing price of a specified stock and alerts you via WhatsApp using the Twilio API if there is a significant price change. 
If the stock price changes by 5% or more compared to the previous day's closing price, the program fetches the latest news related to the company from NewsAPI and sends the top three news headlines, descriptions, and sources to your phone.

**Features**
- Stock Price Monitoring: Retrieves the daily closing prices for a specified stock using the Alpha Vantage API.
- Percentage Change Calculation: Calculates the percentage change in the stock price between yesterday and the day before yesterday.
- News Fetching: Fetches the top three latest news articles related to the specified company using the NewsAPI if there is a significant price change.
- WhatsApp Alerts: Sends an alert via WhatsApp using the Twilio API, including the percentage change and the top three news headlines, descriptions, and sources.
- Environment Variables: Uses environment variables to store sensitive information like API keys and authentication tokens for enhanced security.

**How It Works**

**Fetch Stock Prices:**
- The program fetches the daily stock prices for the specified stock using the Alpha Vantage API.
- It retrieves the closing prices for yesterday and the day before yesterday.
  
**Calculate Percentage Change:**
- The program calculates the percentage change in the stock price between the two days.
  
**Check for Significant Change:**
- If the percentage change is 5% or more, the program proceeds to fetch news articles.
- If the change is less than 5%, it prints a message indicating no significant change.

**Fetch and Display News:**
- The program fetches the top three latest news articles related to the specified company using NewsAPI.
- It formats the news articles with titles, descriptions, and sources.

**Send WhatsApp Alert:**
- The program sends a WhatsApp message with the percentage change and news articles to your specified phone number using the Twilio API.

**Example Output**

**Console Output**

![image](https://github.com/user-attachments/assets/b246714f-68ab-4d13-8538-807887468893)


**WhatsApp Message**

![452036682_873509361351911_1607151668863926382_n](https://github.com/user-attachments/assets/aeb8cd06-1c7e-4eff-8b9c-ed713561f97b)

