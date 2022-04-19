N = int(input("Enter number of students: "))
M = int(input("Enter number of scores: "))

names = []
for i in range(N):
  names.append(input('Enter student name: '))

list2d =[]
for i in range(N):
  name = []
  for j in range(M):
    name.append(int(input("Enter {}'s score: ".format(names[i]))))
  list2d.append(name)

for i in range(N):
  print(names[i], end = " ")
  for j in range(M):
    print(list2d[i][j], end = " ")
  print()

for i in range(N):
  rsum = sum(list2d[i])
  print("{} sum:".format(names[i]), rsum, "\t average:".format(names[i]), "{:.2f}".format(rsum/M))

for i in range(M):
  csum = 0
  for j in range(N):
    csum += list2d[j][i]
  print("Subject {} sum:".format(i+1), csum,"\t average:".format(i+1), "{:.2f}".format(csum/N))