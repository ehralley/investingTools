import mechanize
from bs4 import BeautifulSoup as BS

while 1:
	print "Please Input Stock Symbol: "
	stockSymbolInput = raw_input()
	if stockSymbolInput.isalpha():
		break
	print "Symbol input not a string, please try again"

stockCountry = 'US'
stockSymbol = stockSymbolInput

br = mechanize.Browser()


#Browswer options
#Ignore robots.txt
br.set_handle_robots(False)

# Don't add Referer header
br.set_handle_referer(False)

#Don't handle Refresh redirections
br.set_handle_refresh(False)

#Setting the user agent as Safari
br.addheaders = [('User-agent','Mac Safari')]


response = br.open("http://www.google.com/finance/info?infotype=infoquoteall&q=" + stockSymbol)
print response.read()

response = br.open("http://www.stock2own.com/StockAnalysis/Stock/" + stockCountry + "/" + stockSymbol + "/")
# for form in br.forms():
# 	print form.name
print br.title()
# print br.forms()
