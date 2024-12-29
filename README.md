# Stock and News Alert via SMS

This project fetches the latest stock price changes and news related to a company, then sends the information via SMS using Twilio.

 Features
- Scrapes the current stock price change percentage from Yahoo Finance.
- Fetches the latest news articles related to a company using the News API.
- Sends a message via SMS with the stock price change and the latest news headline.

 Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `twilio` library

1. Obtain API Keys
News API: Create an account on News API and obtain your API key.
Twilio: Sign up for a Twilio account at Twilio. Obtain your Account SID, Auth Token, and a Twilio phone number.
2. Configure the Script
Replace the placeholders in the script with the following:

STOCK_NAME: The stock symbol (e.g., AAPL for Apple).
COMPANY_NAME: The name of the company related to the stock (e.g., Apple).
NEWS_API: Your News API key.
TWILIO_SID: Your Twilio Account SID.
TWILIO_AUTHTOKEN: Your Twilio Auth Token.
FROM NUMBER: The phone number from which the SMS will be sent (this must be a Twilio number).
TO NUMBER: The phone number to which the SMS will be sent.
