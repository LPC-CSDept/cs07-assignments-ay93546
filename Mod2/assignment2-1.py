males = int(input("Enter number of males:"))
females = int(input("Enter number of females:"))

total = males + females
male_percent = float((males/total) *100)
female_percent = float((females/total) *100)

print("The total number of students:\t", total)
print("The number of males and females\t", males, "\t", females)
print("The percentage of males and females\t", '{0}%\t{1}%'.format(male_percent, female_percent))