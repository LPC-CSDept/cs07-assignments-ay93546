'''
#1
scores = {'Kim': [100, 80, 70, 60], 
          'Bill': [100, 90, 80, 60], 
          'Mary': [90, 80, 70, 100]}

sname = input("Enter student name: ")

try:
  i_score = scores[sname]
except KeyError:
  print("Key Error")
else:
  print("{0}'s total score: {1}".format(sname, sum(i_score)))
  print("{0}'s lowest score: {1}".format(sname, min(i_score)))

#2
emp_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
new_dict = {}
for k in keys:
       try:
               new_dict[k] = emp_dict[k]
       except KeyError:
               pass
print (new_dict)

#3
emp_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["age", "city"]
for k in keys:
  emp_dict.pop(k)
print(emp_dict)

#4
emp_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
emp_dict['location'] = emp_dict.pop('city')
print(emp_dict)

#5
dict1 = {'name': 'KIM', 'ZIP':94598, 'address':'1234 Grand ave'}
dict2 = {'score':[100,90], 'Grade':'Senior'}
dict3 = {**dict1, **dict2}

print (dict3)

#6
names  = ['Bill', 'John', 'Kurt']
values = [100, 90, 90]
zip_values = zip(names, values)
for zipval in zip_values:
  print(zipval)
'''
#7
id  = [1001, 1002, 1003]
courses = ['C Programming', 'Java Programming', 'Python Programming']
zip_values = zip(id, courses)
for zipval in zip_values:
  print(zipval)