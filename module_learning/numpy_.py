import numpy as np

##abs
abs(-1)  # 1

##all
np.all([1, 1, 1, 0])  # False

##any
np.any([1, 0, 0, 0])  # True

##arange
x = np.arange(10)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

##array
np.array([1, 2, 3], dtype='f')
# array([ 1.,  2.,  3.], dtype=float32)

##cos

##dot
# matrix product

##eye
d = np.eye(2)  # Create a 2x2 identity matrix
print(d)  # Prints "[[ 1.  0.]
#          [ 0.  1.]]"

##floor

##full
c = np.full((2, 2), 7)  # Create a constant array
print(c)  # Prints "[[ 7.  7.]
#          [ 7.  7.]]"

##histogram
# todo

##hstack
# put arrays together horizontally

##linalg.det()
# calculate Determinate

##linalg.eig()
# calculate Eigenwert

##linalg.inv()
# inverse of a matrix

##linspace
# np.linspace(from, to, n_numbers)
np.linspace(1., 4., 6)
# array([ 1. ,  1.6,  2.2,  2.8,  3.4,  4. ])

##max
np.max([3, 4, 5])  # 5

##min

##ones
b = np.ones((1, 2))  # Create an array of all ones
print(b)  # Prints "[[ 1.  1.]]"

##random 
e = np.random.random((2, 2))  # Create an array filled with random values
print(e)  # Might print "[[ 0.91940167  0.08143941]
#               [ 0.68744134  0.87236687]]"

##reshape
np.arange(30).reshape(5, 6)
#
# array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11],
#       [12, 13, 14, 15, 16, 17],
#       [18, 19, 20, 21, 22, 23],
#       [24, 25, 26, 27, 28, 29]])

##rot90
# rotate matrix 90 degrees

##sin

##sum
np.sum(x)  # sum of all elements

##transpose
# transpose a matrix

##vstack
# put arrays together vertically

##zeros
a = np.zeros((2, 2))  # Create an array of all zeros
print(a)  # Prints "[[ 0.  0.]
#          [ 0.  0.]]"
