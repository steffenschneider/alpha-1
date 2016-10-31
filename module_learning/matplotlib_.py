import matplotlib.pyplot as plt
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
