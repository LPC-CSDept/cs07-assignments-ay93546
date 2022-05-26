import random
from collections import defaultdict
intlist = []
sol = defaultdict(int)

for i in range(10):
  intlist.append(random.randint(0, 4))

for number in intlist:
  sol[number]+=1

biggest = 0
number = 0
for i in sol:
  if(biggest < sol[i]):
    biggest = sol[i]
    number = i
  
print("biggest number:",number,"had",biggest,"duplicates")
print(dict(sol))
