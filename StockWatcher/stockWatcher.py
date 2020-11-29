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
	logging.basicConfig(filename=LOG_FILE,
					    level=logging.INFO,
						format=' %(asctime)s %(message)s ')
	logging.info("StockWatcher - start program")

	# For Step B: Replace the following line with
	# code to get the stock symbols from the command line
	stock_list = sys.argv[1:]
	
	for i in range(len(stock_list)):
		stock = stock_list[i].upper()
		print("Begin watch for " + stock)
		thread = threading.Thread(target = get_quote, args = (stock, ))
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
	
	# For Step C: Replace CODE HERE to get the stock
	# prices from the Yahoo Finance website using
	# requests and Beautiful Soup
	prices = ['20', '25', '30', '30', '30', '20']
	price = prices[0]
	prev_price = '10'

	text = "Start watching " + symbol + ": Price: " + price
	print(text)
	logging.info(text)

	i = 0 # not needed with Step C (remove)

	# Start watching and continue until CTRL-Break
	while True:
	
		# Get Price with Steps A and B only
		# Step C use requests and Beautiful Soup
		price = prices[i%6]

		# Send price for symbol to log
		logging.info(symbol + "\t" + price)

		i = i + 1 # not needed with Step C (remove)

		# Check for price difference and send email,
		# if different
		if price != prev_price:
			text = symbol + " now at " + price + \
				   "; was " + prev_price
			print(text)
			send_email(text)
			prev_price = price

		time.sleep(WAIT_INTERVAL)
		
def send_email(msg):
	"""
	Simulate sending an email with simple print()
	"""
	print("sendEmail: " + msg)
	
main() 