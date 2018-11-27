from xml.dom.minidom import parse, parseString
import sys
import csv
import re
import os

dom1 = parse(sys.argv[1])  # parse an XML file by name

#find table with classname mdcTable
tables = dom1.getElementsByTagName("table")

table = dom1.createElement("foo")
for t in tables:
	if 'class' in t.attributes:
		if t.attributes['class'].nodeValue == 'mdcTable':
			table = t
			break

#get col labels
labelRow = table.firstChild
labels = ["exchange", "symbol", "company", "volume", "price", "change"]
addHeaders = not os.path.isfile('stocks.csv') #if it exists, dont add rows

with open("stocks.csv", "a") as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	# reader = csv.reader(csvfile)
	if addHeaders: #if first time (file creation), write header rowss
		writer.writerow(labels)
	colArr = []
	for n, row in enumerate(table.childNodes, start=0):
		if n == 0: #skip header row
			continue
		#add exchange name to each row
		colArr.append('Nasdaq')
		for i, col in enumerate(row.childNodes, start=0):

			if i != 0 and i!=5: #ignore first and last col

				if i == 1: #name col behaves different
					if n!= 0:
						name = col.childNodes[1].firstChild.data
						name = name[:-1] #ignore last item \n

						#extract symbol
						pattern = re.compile('\(\w*\)')
						match = pattern.search(name)
						symbol = match.group(0)[1:-1]

						#remove symbol from name
						end = match.regs[0][0] #start index of regex match
						name = name[0:(end - 1)] #accounting for space
						colArr.append(name)
						colArr.append(symbol)

				elif i == 2: #remove commas from volume col
					if n != 0: #ignore the header row
						num = int(col.firstChild.data.replace(',', ''))
						colArr.append(num)
				else:
					colArr.append(col.firstChild.data)
		#finished row loop
		writer.writerow(colArr)
		colArr = []
	#finished table loop

#end of script
sys.exit()