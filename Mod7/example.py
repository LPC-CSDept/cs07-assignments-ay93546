import xlrd
from functools import reduce

wb = xlrd.open_workbook('Mod7/student.xls')
ws = wb.sheet_by_index(0)

keys = ws.row_values(0)
sname = []
for i in range(ws.nrows):
	sname.append(ws.row_values(i)[0])

scores_list = []
for x in range(ws.nrows):
  scores = []
  for p in range(1, ws.ncols):
    scores.append(int(ws.row_values(x)[p]))
  scores_list.append(scores)

dict1 = dict(zip(sname, scores_list))
for k, v in dict1.items():
  print(k, v)

def filter1(val):
  ssum = sum(val)
  return True if ssum > 290 else False

filterobj = filter(filter1, dict1.values())
for value in filterobj:
  for k, v in dict1.items():
    if v == value:
      print(k)

#idec anymore