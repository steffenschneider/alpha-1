## subplot
from pylab import *

x = linspace(-5, 5, 1000)
y = sin(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.plot(y)
plt.grid(True)
plt.xlabel('...')
plt.ylabel('...')
plt.show()

## trendline
import numpy as np
import matplotlib.pyplot as plt

# make up some data
x = [1, 2, 3]
y = [22, 23, 20]

# plot
plt.scatter(x, y)

# beautify the x-labels, turn 45 degrees
plt.gcf().autofmt_xdate()

# calc the trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")

plt.show()
