import random
even = False
prev = random.randint(0, 100)
while True:
  if prev % 2 == 0:
    even = True
  next = random.randint(0, 100)
  if next % 2 == 0 and even:
    print(prev, next)
    break
  else:
    even = False
    prev = next