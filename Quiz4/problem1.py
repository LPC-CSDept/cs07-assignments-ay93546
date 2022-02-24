import random
even = False
while True:
  prev = random.randint(0, 100)
  if prev % 2 == 0:
    even = True
  next = random.randint(0, 100)
  if next % 2 == 0 and even:
    print(prev, next)
    break
