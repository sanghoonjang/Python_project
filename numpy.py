
# How to use Numpy

import numpy as np

# Way to make 1 demention array
a = np.array([0, 1, 2, 3, 4, 5]) # array([0, 1, 2, 3, 4, 5])
b = np.arange(6) # array([0, 1, 2, 3, 4, 5])

# Way to make 2 demention array
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


# Basic Operations
a = np.array([[10,20,30],[40,50,60]])
b = np.arange(6).reshape(2,3)

  # Add
a + b # array([[10, 21, 32],
                   [43, 54, 65]])

  # Multiplication
a * b # array([[  0,  20,  60],
               [120, 200, 300]])

a.dot(b) # same with a * b
np.dot(a,b) # same with a * b

  # *= +=
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3)) # array([[ 0.24294393,  0.16317671,  0.59804338],
                                     [ 0.45268083,  0.55809006,  0.81551643]])

a *= 3
a # array([[3, 3, 3],
           [3, 3, 3]])
b += a
b # array([[ 3.24294393,  3.16317671,  3.59804338],
           [ 3.45268083,  3.55809006,  3.81551643]])

  # sum, max, min
a = np.random.random((2,3)) # array([[ 0.63860985,  0.90263005,  0.0869552 ],
                                     [ 0.73616405,  0.16258958,  0.11571384]])
a.sum() # 2.6426625714576595
a.max() # 0.90263004713944162
a.min() # 0.086955203097858313

b = np.arange(9).reshape((3,3)) # array([[0, 1, 2],
                                         [3, 4, 5],
                                         [6, 7, 8]])
b.sum(axis=0) # array([ 9, 12, 15])
b.sum(axis=1) # array([ 3, 12, 21])
b.cumsum(axis=1) # array([[ 0,  1,  3],
                          [ 3,  7, 12],
                          [ 6, 13, 21]])

