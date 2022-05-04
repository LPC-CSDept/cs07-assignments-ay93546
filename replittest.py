dictionary1 = { 10:"Kurt", 20:"Jim", 30:"Bill"}
print (dictionary1)

unzipped = zip(*dictionary1.items())

for values in unzipped:
       print (values)

IDlist, Namelist = zip(*dictionary1.items())
print (IDlist)  # tuple
print (Namelist) # tuple


list1 = [[1,2,3,4,5], [11,12,13,14,15]]

zipobj = zip(*list1)
print (zipobj)
for v in zipobj:
	print (v)
	