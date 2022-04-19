scores = {'Kim': [100, 80, 70, 60], 
          'Bill': [100, 90, 80, 60], 
          'Mary': [90, 80, 70, 100]}

sname = input("Enter student name: ")

i_score = scores[sname]
print("{0}'s total score: {1}".format(sname, sum(i_score)))
print("{0}'s lowest score: {1}".format(sname, min(i_score)))