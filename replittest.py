#5-1
import random
def generate():
  n = random.randint(1, 10)
  list1 = []
  list2 = []
  for i in range(n):
    list1.append(random.randint(0, 9))
    list2.append(random.randint(0, 9))
  return list1, list2  
def sumProduct(l1, l2):
  product_list = []
  for i in range(len(l1)):
    product_list.append(l1[i] * l2[i])
  return sum(product_list)

if __name__ == '__main__':
  list1, list2 = generate()  
  result = sumProduct(list1, list2)
  print(list1)
  print(list2)
  print(result)

#5-2
def stripspace(str):
  res = ''
  for letter in str:
    if letter.isupper():
      res += letter      
  return res
if __name__ == '__main__':
  message = input('Enter string: ')
  result = stripspace(message)
  print(result)

#5-3
isspace = lambda char: char.isspace()
def mystrip(msg):
  res = ''
  for char in msg:
    if isspace(char) == False:
      res += char
  return res
if __name__ == '__main__':
  msg = input('Enter message: ')
  res = mystrip(msg)
  print (res)

#5-4
def getalnum(msg):
  for char in msg:
    if char.isalnum():
      yield char
msg = 'Python programming section 2'
res = getalnum(msg)
for v in res:
	print (v)