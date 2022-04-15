list1 = [1, 3, 4, 5, 6]
list2 = [2, 4, 5, 6, 7]
getevens = lambda num: num % 2 == 0
def getmerged(list1, list2):
  result = []
  for num in list1:
    if getevens(num) == True:
      result.append(num)
  for num in list2:
    if getevens(num) == True:
      result.append(num)
  for num in result:
    yield num

result = getmerged(list1, list2)
for v in result:
  print(v)