import xlrd

wb = xlrd.open_workbook('Mod7/imdb.xls')
ws = wb.sheet_by_index(0)
rows = [] 

keys = ws.row_values(0)

list1 = []
for j in range(1, ws.nrows):
  dict1 = {}
  for i in range(len(keys)):
    dict1[keys[i]] = ws.row_values(j)[i]
  list1.append(dict1)
print("---------")
print(list1)

# for zed in range(1, ws.nrows):
#   if 1930 < list1[zed('birthYear')] < 1950:
#     print(list1[zed])

for i in range(len(list1)):
	if ( list1[i]['birthYear'] >= 1930 ) and ( list1[i]['birthYear'] <= 1950 ):
		print ('------------', list1[i]['primaryName'])
  