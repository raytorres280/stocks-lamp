from xml.dom.minidom import parse, parseString
import sys
import csv


dom1 = parse(sys.argv[1])  # parse an XML file by name

#third table is the values
table = dom1.getElementsByTagName("table")[2]

#get col labels
labelRow = table.childNodes[0]
labels = []

#no header for row/rank number
labels.append("rank")
#loop thru first row to get col headers
for label in labelRow.childNodes:
	labels.append(label)

table.childNodes[0].childNodes[0].childNodes[0].data = "rank"

with open("stocks.csv", "w") as csvfile:
	writer2 = csv.DictWriter(csvfile, fieldnames=labels)
	rowObj = {}
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	colArr = []
	for n, row in enumerate(table.childNodes):
		for i, col in enumerate(row.childNodes, start=0):
			if i == 1: #name col behaves different
				if n!= 0:
					colArr.append(col.childNodes[1].childNodes[0].data)
				else: #header row name col behaves diff
					colArr.append(col.childNodes[0].data)
			else:
				colArr.append(col.childNodes[0].data)
		#finished row loop
		writer.writerow(colArr)
		colArr = []
	#finished table loop