STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY="Your api"
NEWS_API_KEY="YOUR API KEY"
import requests
from datetime import datetime, timedelta


# Function to find the most recent trading date available
def get_last_trading_day(date):
    while str(date) not in Time_series:  # if weekend/holiday
        date -= timedelta(days=1)
    return str(date)


# SAMPLE API LINK  https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":API_KEY
}
response=requests.get(url=STOCK_ENDPOINT,params=parameter)
response.raise_for_status()
data=response.json()
Time_series=data["Time Series (Daily)"]
today = datetime.today().date()
# Yesterday_data=Time_series[]

yesterday = get_last_trading_day(today - timedelta(days=1))
# Day before yesterday
day_before = get_last_trading_day(today - timedelta(days=2))
Yesterday_data=Time_series[yesterday]
Day_before_yesterday=Time_series[day_before]
print(Yesterday_data)
#---Now we will get the difference here
yesterday_close=float(Yesterday_data["4. close"])
day_before_close=float(Day_before_yesterday["4. close"])
Difference=abs(yesterday_close-day_before_close)
percentage_diff=(Difference/day_before_close)*100
print(f"This is the differen in Tesla stock price {percentage_diff} %")
## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
news_parameter={
    "apiKey":NEWS_API_KEY,
    "qinTitle":COMPANY_NAME
}
news_rep=requests.get(url=NEWS_ENDPOINT ,params=news_parameter)
news_rep.raise_for_status()
news_articles=news_rep.json()["articles"]


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.
three_articles=news_articles[:3]
#this list comprehension will only save top there data sets


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

