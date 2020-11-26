import sys, time
import requests, bs4
import threading, logging
from random import *


# constants used
WAIT_INTERVAL = 120
LOG_FILE = 'stockPriceLog.txt'

def main():
    """
    Clear the log, set up logging, log a start message
    Retrieve the list of stock symbols from the command
    line
    Start up a thread for each stock listed
    Sleep a little to allow the stock prices to be logged
    Have the user enter CTRL-C to stop the program.
    """

    open(LOG_FILE, 'w').close()
    logging.basicConfig(filename=LOG_FILE,level=logging.INFO,format=' %(asctime)s %(message)s ')
    logging.info("StockWatcher - start program")

    stock_list = ["MSFT","GOOG","AAPL","AMZN"]

    for i in range(len(stock_list)):
        stock = stock_list[i].upper()
        print("Begin watch for " + stock)
        thread = threading.Thread(target = get_quote,args = (stock, ))
        thread.setDaemon(True)
        thread.start()
    time.sleep(5) # Sleep for threads to print msgs
    # Need a try-except to catch the ctrl-c ...
    try:
        input("\nHit CTRL-C to stop recording.\n\n")
    except:
        pass
    logging.info("StockWatcher - end program")

def get_quote(symbol):
 """
 Get a stock quote for the given stock symbol using
 Python requests and BeautifulSoup modules.
 Determine the availability of webpage
 Request the quote every WAIT_INTERVAL minutes until the
 user ends the program with CTRL-C
 Compare current quote with previous quote and send
 text when different.
 """

def get_prices(stocks):
    format_url = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=l1"
    stock_string = ",".join(stocks)
    url = format_url % stock_string
    prices = [float(x) for x in requests.get(url).content.split()]
    price_dict = dict(zip(stocks, prices))
    return price_dict

prices = ['20', '25', '30', '30', '30', '20']
price = prices[0]
prev_price = '10'

text = "Start watching " + symbol + ": Price: " + price
print(text)
logging.info(text)
