import mechanize
from bs4 import BeautifulSoup




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


while 1:
	try:
		print "Please Input Stock Symbol: "
		stockSymbolInput = raw_input()
		response = br.retrieve("http://www.google.com/finance/info?infotype=infoquoteall&q=" + stockSymbolInput, 'GoogleData.txt')
	except:
		print "Google can't find that stock symbol, try again"
	else:
		break

print "working..."
file = open("GoogleData.txt","r")
for line in file.readlines():
	if line.find('''"e" :''') != -1:
		exchangeName = (line.split('''"'''))[3]
file.close()

usExchanges = ['NASDAQ','NYSE','AMEX']
canExchanges = ['TSE']

if exchangeName.upper() in usExchanges:
	stockCountry = 'US'
elif exchangeName.upper() in canExchanges:
	stockCountry = 'CA'

br.open("http://www.stock2own.com/StockAnalysis/Stock/" + stockCountry + "/" + stockSymbolInput + "/")
soup = BeautifulSoup(br.response().read(), "html.parser")

table = soup.find("table", id="RawFinData_Ann")
# print table


roicList = []

tableHead = soup.find("thead")
roicName = soup.find("abbr", title="*Return on Invested Capital")

for date, value in zip(tableHead.stripped_strings, roicName.parent.parent.stripped_strings):
	try:
		roicList.append([date,float(value)])
	except:
		continue

print "Annual ROIC Data for " + stockSymbolInput.upper()
for element in roicList:
	print element[0] + ": " + "%.2f" % (element[1])


# print soup.find_all(string="ROIC")



