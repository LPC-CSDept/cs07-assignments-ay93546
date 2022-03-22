'''
import random
r = int(input("Enter row amount: "))
c = int(input("Enter column amount: "))

list2d = []
for i in range(r):
  row = []
  for j in range(c):
    row.append(random.randint(0, 100))
  list2d.append(row)

for i in range(r):
  for j in range(c):
    print(list2d[i][j], end = " ")
  print()

maxr = 0
maxc = 0
for i in range(r):
  rsum = sum(list2d[i])
  print("R{} sum:".format(i+1), rsum)
  if rsum > maxr:
    maxr = rsum

for i in range(c):
  csum = 0
  for j in range(r):
    csum += list2d[j][i]
  print("C{} sum:".format(i+1), csum)
  if csum > maxc:
    maxc = csum

print("Max RSum:", maxr, "\t", "Max CSum:", maxc)
'''
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
label = ['Math', 'English', 'Physics', 'Computer']
bill = [100, 90, 80, 60]
mary = [90, 80, 70, 100]
ax.bar(label, bill, label = 'Bill')
ax.bar(label, mary, bottom = bill, label = 'Mary')
ax.set_xticks(label)
ax.set_title("Stacked graph for scores")
ax.legend()
plt.show()