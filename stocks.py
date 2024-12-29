from twilio.rest import Client
import requests
from bs4 import BeautifulSoup

STOCK_NAME = "STOCK NAME HERE"  # Replace with the stock symbol you want
COMPANY_NAME = "COMPANY NAME HERE"

NEWS_API = "NEWS API HERE"  # Replace with your News API key
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

TWILIO_SID = "TWILIO SID HERE"
TWILIO_AUTHTOKEN = "TWILIO AUTHTOKEN HERE"

# Yahoo Finance URL for the stock
YAHOO_FINANCE_URL = f"https://finance.yahoo.com/quote/{STOCK_NAME}"

# Scrape stock data
response = requests.get(YAHOO_FINANCE_URL)
if response.status_code != 200:
    print("Error fetching stock data")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Extract stock price or change percentage (adjust selectors as needed)
try:
    price_change_element = soup.find('fin-streamer', attrs={'data-field': 'regularMarketChangePercent'})
    percent_change = float(price_change_element.text.strip('()%'))  # Remove percentage sign
except AttributeError:
    print("Could not find stock change percentage.")
    exit()

if percent_change > 0:
    text = f"⬆️  {percent_change}%"
else:
    text = f"⬇️  {percent_change}%"

news_params = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)

if news_response.status_code != 200:
    print("Error fetching news data")
    exit()

news = news_response.json()["articles"]
first_news = str(news[0]) if news else "No news available"

combined_message = f"{text} {first_news}"

print(combined_message)


client = Client(TWILIO_SID, TWILIO_AUTHTOKEN)

message = client.messages.create(
    from_='+FROM NUMBER',
    body=combined_message,
    to='+TO NUMBER'
)
