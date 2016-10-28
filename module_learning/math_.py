import math

import numpy as np
import pylab as p

## acos
# Spiegelung an der Winkelhalbierenden von cos
print(math.acos(0))  # 1.57079 # angle in rad
print(math.degrees(1.57079))  # 89.999

## degrees
# rad to degrees
print(math.degrees(1.5707963267948966))  # 90.0

## e
# Eulersche Zahl
print(math.e)  # 2.718281828459045

## exp
print(math.exp(1))  # 2.718281828459045

## factorial
print(math.factorial(4))  # 24
print(math.factorial(5))  # 120

## radians
# degrees to rad
print(math.radians(90))  # 1.5707963267948966

## tan
x = p.linspace(-1.0, 1.0, 1000)
y = (p.sin(2 * p.pi * x)) / (p.cos(2 * p.pi * x))

np.seterr(invalid='ignore')
tol = 10
y[y > tol] = np.nan
y[y < -tol] = np.nan

# p.plot(x, y, 'g-', lw=1)
# p.show()

##trunc
# drop fractional part of x
