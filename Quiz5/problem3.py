import matplotlib.pyplot as plt
import numpy as np

label = ['Bill', 'Jim', 'Joe']
width = 0.15
x = np.arange(3)
math = [100, 100, 100]
english = [90, 90, 80]
physics = [90, 80, 90]
computer = [90, 80, 90]

fig, ax = plt.subplots()
s1 = ax.bar(x-width*1.5, math, width, label = 'Math')
s2 = ax.bar(x-width*0.5, english, width, label = 'English')
s3 = ax.bar(x+width*0.5, physics, width, label = 'Physics')
s4 = ax.bar(x+width*1.5, computer, width, label = 'Computer')

ax.legend(loc = 'lower center')
ax.set_title('Grouped graph for scores')
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.bar_label(s1, padding=3)
ax.bar_label(s2, padding=3)
ax.bar_label(s3, padding=3)
ax.bar_label(s4, padding=3)
plt.show()