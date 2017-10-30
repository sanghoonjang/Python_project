
# How to use Numpy

import numpy as np

# Way to make an 1 demention array
a = np.array([0, 1, 2, 3, 4, 5]) # array([0, 1, 2, 3, 4, 5])
b = np.arange(6) # array([0, 1, 2, 3, 4, 5])

# Way to make an 2 demention array
a1 = np.array([[0, 1, 2],[3, 4, 5]]) # array([[0, 1, 2],
                                          [3, 4, 5]])
b1 = np.arange(6).reshape(2, 3) # array([[0, 1, 2],
                                        [3, 4, 5]])

a.reshape(2, 3) # array([[0, 1, 2],
                        [3, 4, 5]])

# To create sequences of numbers
np.arange(10, 30, 5) # array([10, 15, 20, 25])
np.linspace(0, 2, 9) # array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])

np.zeros( (2, 3) ) # array([[ 0.,  0.,  0.],
                       [ 0.,  0.,  0.]]) 
np.ones( (2, 3) ) # array([[ 1.,  1.,  1.],
                        [ 1.,  1.,  1.]])


# Basic Operations¶

