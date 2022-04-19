#e1
user_list = []
sum = 0
for i in range(5):
  user_num = int(input("Enter number: "))
  user_list.append(user_num)
  sum += user_num
sum = sum - max(user_list) - min(user_list)
average = sum / 5
print("Sum:", sum, "Average:", average)

#e2
import random
num_list = []
for i in range(10):
  num_list.append(random.randint(0, 100))
print(num_list)
print("Min:", min(num_list), "Index:", num_list.index(min(num_list)))

#e3
import random
num_list = []
for i in range(10):
  num_list.append(random.randint(0, 100))
average = sum(num_list)/ len(num_list)
count = 0
for i in range(len(num_list)):
  if num_list[i] > average:
    count += 1
print(count)

#e4
import random
list1 = []
list2 = []
result_list = []
for i in range(10):
  list1.append(random.randint(0, 100))
  list2.append(random.randint(0, 100))
  sum = list1[i] + list2[i]
  result_list.append(sum)
print(list1)
print(list2)
print(result_list)

#e5
import random
list = []
result_list = []
for i in range(10):
  list.append(random.randint(0, 100))
for i in range(0, len(list), 2):
  result_list.append(list[i])
print(list, result_list)

#e6
name_list = []
for i in range(5):
  name = input("Enter name: ")
  name_list.append(name)
  if "J" in name_list[i] or 'j' in name_list[i]:
    print(name_list[i])

#e7
list = []
import random
for i in range(10):
  list.append(random.randint(0, 100))
user_input = int(input("Enter value: "))
print(list)
list.sort()
print(list)
list.insert(0, user_input)
list.sort()
print(list)

#e8
import random
num_list = []
for i in range(10):
  num_list.append(random.randint(0, 100))
i = int(input("Enter i value: "))
num_list.sort()
print(num_list)
print(num_list[i-1])

#e9
import random
num_list = []
for i in range(10):
  num_list.append(random.randint(0, 100))
i = int(input("Enter i value: "))
print(num_list)
for i in range(i-1):
  num_list.remove(min(num_list))
print(min(num_list))
