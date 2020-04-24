import matplotlib
import matplotlib.pyplot as plt
import numpy as np


import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 2, 34, 45, 25]

lines = plt.plot(x, y)
plt.setp(lines[0])
plt.legend(('No mask',), loc='upper right')
plt.grid()
plt.title('Masked line demo')
plt.savefig("a.png")
