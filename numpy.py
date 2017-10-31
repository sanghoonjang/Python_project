
# How to use Numpy

import numpy as np

# Way to make 1 demention array
a = np.array([0, 1, 2, 3, 4, 5]) # array([0, 1, 2, 3, 4, 5])
b = np.arange(6) # array([0, 1, 2, 3, 4, 5])

# Way to make 2 demention array
a1 = np.array([[0, 1, 2],[3, 4, 5]]) """ array([[0, 1, 2],
                                                [3, 4, 5]])"""
b1 = np.arange(6).reshape(2, 3) """ array([[0, 1, 2],
                                           [3, 4, 5]])"""
a.reshape(2, 3) """ array([[0, 1, 2],
                           [3, 4, 5]])"""

  
# To create sequences of numbers
np.arange(10, 30, 5) # array([10, 15, 20, 25])
np.linspace(0, 2, 9) # array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])

np.zeros( (2, 3) ) """ array([[ 0.,  0.,  0.],
                              [ 0.,  0.,  0.]])""" 
np.ones( (2, 3) ) """ array([[ 1.,  1.,  1.],
                             [ 1.,  1.,  1.]])"""


# Basic Operations
a = np.array([[10,20,30],[40,50,60]])
b = np.arange(6).reshape(2,3)

  # Add
a + b """ array([[10, 21, 32],
                 [43, 54, 65]])"""

  # Multiplication
a * b """ array([[  0,  20,  60],
                 [120, 200, 300]])"""

a.dot(b) # same with a * b
np.dot(a,b) # same with a * b

  # *= +=
a = np.ones((2,3), dtype=int)
b = np.random.random((2,3)) """ array([[ 0.24294393,  0.16317671,  0.59804338],
                                       [ 0.45268083,  0.55809006,  0.81551643]])"""

a *= 3
a """ array([[3, 3, 3],
             [3, 3, 3]])"""
b += a
b """ array([[ 3.24294393,  3.16317671,  3.59804338],
             [ 3.45268083,  3.55809006,  3.81551643]])"""

  # sum, max, min
a = np.random.random((2,3)) """ array([[ 0.63860985,  0.90263005,  0.0869552 ],
                                       [ 0.73616405,  0.16258958,  0.11571384]])"""
a.sum() # 2.6426625714576595
a.max() # 0.90263004713944162
a.min() # 0.086955203097858313

b = np.arange(9).reshape((3,3)) """ array([[0, 1, 2],
                                          [3, 4, 5],
                                          [6, 7, 8]])"""
b.sum(axis=0) # array([ 9, 12, 15])
b.sum(axis=1) # array([ 3, 12, 21])
b.cumsum(axis=1) """ array([[ 0,  1,  3],
                            [ 3,  7, 12],
                            [ 6, 13, 21]])"""


# Indexing, Slicing and Iterating
a = np.arange(10)**3
a # array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
b = np.arange(9).reshape((3,3))
b """ array([[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]])"""

  # Indexing
a[3] # 27

  # Slicing
a[2:5] # array([ 8, 27, 64])
a[0:6:2] = -1000 # array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
a[::-1] # array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000]) >> Reversed a
b[0:2,0:2] """ array([[0, 1],
                      [3, 4]]) >>> 2D Slicing"""

# Shape Manipulation
a = np.floor(10*np.random.random((3,4)))
a """ array([[ 3.,  2.,  3.,  0.],
             [ 2.,  0.,  2.,  3.],
             [ 4.,  1.,  9.,  5.]])"""
a.ravel() # array([ 3.,  2.,  3.,  0.,  2.,  0.,  2.,  3.,  4.,  1.,  9.,  5.])
a.reshape(6,2) """ array([[ 3.,  2.],
                          [ 3.,  0.],
                          [ 2.,  0.],
                          [ 2.,  3.],
                          [ 4.,  1.],
                          [ 9.,  5.]])"""
a.T """ array([[ 3.,  2.,  4.],
               [ 2.,  0.,  1.],
               [ 3.,  2.,  9.],
               [ 0.,  3.,  5.]])"""
a.shape # (3, 4)
a.T.shape # (4, 3)

a.resize(2, 6) """ array([[ 3.,  2.,  3.,  0.,  2.,  0.],
                          [ 2.,  3.,  4.,  1.,  9.,  5.]])"""

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
a.reshape(3, -1) """Only reshape >> array([[ 3.,  2.,  3.,  0.],
                                           [ 2.,  0.,  2.,  3.],
                                           [ 4.,  1.,  9.,  5.]])"""

# Stacking together different arrays
a = np.floor(10*np.random.random((2,2)))
a """ array([[ 0.,  4.],
             [ 7.,  8.]])"""
b = np.floor(10*np.random.random((2,2)))
b """ array([[ 4.,  4.],
             [ 2.,  7.]])"""

np.vstack((a,b)) """ array([[ 0.,  4.],
                            [ 7.,  8.],
                            [ 4.,  4.],
                            [ 2.,  7.]]) """
np.hstack((a,b)) """ array([[ 0.,  4.,  4.,  4.],
                            [ 7.,  8.,  2.,  7.]])"""

a = np.array([1,2])
a # array([1, 2])
a[:,newaxis] """ array([[1],
                        [2]])"""

# Splitting one array into several smaller ones
a = np.floor(10*np.random.random((2,12)))
a """ array([[ 2.,  0.,  7.,  3.,  0.,  2.,  5.,  0.,  5.,  4.,  9.,  5.],
             [ 6.,  7.,  1.,  9.,  1.,  6.,  8.,  6.,  8.,  5.,  4.,  4.]])"""

np.hsplit(a,3) """[array([[ 2.,  0.,  7.,  3.],
                         [ 6.,  7.,  1.,  9.]]), array([[ 0.,  2.,  5.,  0.],
                         [ 1.,  6.,  8.,  6.]]), array([[ 5.,  4.,  9.,  5.],
                         [ 8.,  5.,  4.,  4.]])]"""


# Copies and Views
a = np.arange(12)
a # array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

b = a
b is a # Ture

b.shape = 2,6
b """ array([[ 0,  1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10, 11]])"""
a """ array([[ 0,  1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10, 11]])"""

  # View()
c = a.view()
c """ array([[ 0,  1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10, 11]])"""

c is a # False
c.base is a # True
c.flags.owndata # False >>> The data c has is not c's own data

c.shape = 3,4
c """ array([[ 0,  1,  2,  3],
             [ 4,  5,  6,  7],
             [ 8,  9, 10, 11]])"""
a """ array([[ 0,  1,  2,  3,  4,  5],
             [ 6,  7,  8,  9, 10, 11]]) >>> a is not changed!! """

c[1,3] = -1000
c """ array([[    0,     1,     2,     3],
             [    4,     5,     6, -1000],
             [    8,     9,    10,    11]])"""
a """ array([[    0,     1,     2,     3,     4,     5],
             [    6, -1000,     8,     9,    10,    11]]) >>> The value changed in 'c array' is also changed in 'a array'. """

  # Sliced array
s = a[0:2,2:4]
s """ array([[2, 3],
             [8, 9]]) """
s[:] = 10
s """ array([[10, 10],
             [10, 10]])"""
a """ array([[    0,     1,    10,    10,     4,     5],
             [    6, -1000,    10,    10,    10,    11]])"""
 # Deep copy
d = a.copy()
d """ array([[    0,     1,    10,    10,     4,     5],
             [    6, -1000,    10,    10,    10,    11]]) """
d is a # False
d.base is a # False
d.flags.owndata # True
d[:] = 0
d """ array([[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]) """
a """ array([[    0,     1,    10,    10,     4,     5],
             [    6, -1000,    10,    10,    10,    11]]) """
