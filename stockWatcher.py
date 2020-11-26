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
