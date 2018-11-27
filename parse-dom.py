from xml.dom.minidom import parse, parseString
import sys
import csv


dom1 = parse(sys.argv[1])  # parse an XML file by name

#third table is the values
table = dom1.getElementsByTagName("table")[2]

#get col labels
labelRow = table.firstChild
labels = []

#no header for row/rank number
labels.append("Rank")
#loop thru first row to get col headers
for label in labelRow.childNodes:
	labels.append(label)

table.firstChild.firstChild.firstChild.data = "rank"

with open("stocks.csv", "w") as csvfile:
	writer = csv.writer(csvfile, delimiter=',')
	colArr = []
	for n, row in enumerate(table.childNodes):
		for i, col in enumerate(row.childNodes, start=0):
			if i == 1: #name col behaves different
				if n!= 0:
					name = col.childNodes[1].firstChild.data
					name = name[:-1] #ignore last item \n
					colArr.append(name)
				else: #header row name col behaves diff
					colArr.append(col.firstChild.data)

			elif i == 2: #remove commas from volume col
				if n != 0: #ignore the header row
					num = int(col.firstChild.data.replace(',', ''))
					colArr.append(num)
				else:
					colArr.append(col.firstChild.data)
			else:
				colArr.append(col.firstChild.data)
		#finished row loop
		writer.writerow(colArr)
		colArr = []
	#finished table loop

#end of script
sys.exit()