from functools import reduce
caFile = open('final/ca2021.txt')
flFile = open('final/fl2021.txt')

#question 1-1
caMale = []
caMaleNum = []
caFemale = []
caFemaleNum = []

flMale = []
flMaleNum = []
flFemale = []
flFemaleNum = []

allData = []
labels = ["state","name","gender","number"]

for line in caFile:
  line = line.replace("\n","")
  line = line.split(" ")
  caMale.append(line[1])
  caMaleNum.append(line[2])
  caFemale.append(line[3])
  caFemaleNum.append(line[4])

for line in flFile:
  line = line.replace("\n","")
  line = line.split(" ")
  flMale.append(line[1])
  flMaleNum.append(line[2])
  flFemale.append(line[3])
  flFemaleNum.append(line[4])

#question 1-2
for i in range(len(flMale)):
  data = ["FL"]+[flMale[i]]+["Male"]+[flMaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(flFemale)):
  data = ["FL"]+[flFemale[i]]+["Female"]+[flFemaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(caMale)):
  data = ["CA"]+[caMale[i]]+["Male"]+[caMaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(caFemale)):
  data = ["CA"]+[caFemale[i]]+["Female"]+[caFemaleNum[i]]
  allData.append(dict(zip(labels,data)))

#question 1-3
caMales = list(filter(lambda x: x['state'] == 'CA' and x['gender'] == 'Male', allData))


for male in caMales:
  male["number"] = int(male["number"].replace(",",""))

caMales = sorted(caMales, key=lambda x: x['number'], reverse=True)

for male in caMales:
  male["number"] = str(male["number"])

for people in caMales[:10]:
  print(people)

print("-------------------------------------")

  
flFemales = list(filter(lambda x: x['state'] == 'FL' and x['gender'] == 'Female', allData))

for female in flFemales:
  female["number"] = int(female["number"].replace(",",""))

flFemalesE = list(filter(lambda x: x['name'][0]=="E", flFemales))
flFemalesE = sorted(flFemalesE, key=lambda x: x['number'], reverse=True)
#print(flFemalesE)

for people in flFemalesE[:10]:
  print(people)

print("-------------------------------------")

#question 1-4
for female in flFemales:
  female["number"] = str(female["number"])
flFemales = list(map(lambda x:int(x['number'].replace(",","")),flFemales[:10]))
sumnum = lambda x,y: x+y
totalNumber = reduce(sumnum, flFemales, 0)
print(totalNumber)