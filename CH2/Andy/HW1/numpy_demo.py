# demo of numpy

import numpy as np

# INITIALIZE

x = np.zeros(5)
'''>>> [0. 0. 0. 0. 0.]'''  # . means Float

x = np.ones(5, dtype=int)  # dtype claims type to be int
'''>>> [1 1 1 1 1]'''

x = np.array([1, 2, 3])  # can also input tuple
'''>>> [1 2 3]'''

x = np.empty(4)  # Filled by random num
'''>>> [1.5e-323 4.0e-323 4.0e-323 4.0e-323]'''

x = np.linspace(2, 20, 10)
# Create np array [2, 20] (closing) with 10 items, default to be Float
'''>>> [ 2.  4.  6.  8. 10. 12. 14. 16. 18. 20.]'''

x = np.array([[1, 2, 3], [4, 5, 6]])  # 2d
'''>>> [[1 2 3]
        [4 5 6]]'''

x.shape
'''>>> (2, 3)'''  # (nrow, ncol)

x.reshape(-1, 1)  # this is a 'return', not 'mutate'
'''
>>> [[1]
     [2]
     [3]
     [4]
     [5]
     [6]]'''
# reshape to (6,1) when the other val can be -1 as default

x = np.zeros([4, 3])  # [nrow, ncol]
''' 
>>> [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]
'''

x = np.random.randint(1, 2, size=2)
# sample int from [1,2), open is due to sampling alg
'''>>> [1 1]'''

x = np.random.randint(1, 2, size=[2, 3])
# sample from [1,3) and fill with (2,3) np array
'''
>>> [[1 1 1]
     [1 1 1]]
'''
np.random.seed(123)
x = np.random.randint(
    [0, 2, 5],
    [1, 4, 10],
    size=[4, 3],
)
# sample from [0,1) for col1
# sample from [2,4) for col2
# sample from [5,10) for col3
'''
>>> [[0 2 7]
     [0 2 7]
     [0 2 6]
     [0 3 7]]
'''

# Slicing & other selection functionality
x = np.array(range(10))
x[x % 2 != 0]  # Note cannot use x%2, it will map every item
'''>>> [1, 3, 5, 7, 9]'''

x = np.where(x % 2, 'odd', 'even')
# Here we can use x%2, False(0) gives even, True(!=0) gives odd
'''>>> ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']'''
x = np.array([[0, 2, 7], [0, 2, 7], [0, 2, 6], [0, 3, 7]])

x[0:2]  # select [0,2) rows
'''
>>> [[0 2 7]
     [0 2 7]]
 '''

x[:, 0:2]  # : means select all, here, select [0,2) cols
'''
>>> [[0 2]
     [0 2]
     [0 2]
     [0 3]]
'''

x[::2, ::2]  # stepsize is 2 for row and col
'''
>>> [[0 7]
     [0 6]]
'''

x[::-1]  # reverse the order of row
'''
>>> [[0 3 7]
     [0 2 6]
     [0 2 7]
     [0 2 7]]
'''

x[:, ::-1]  # reverse the order of col
'''
>>> [[7 2 0]
     [7 2 0]
     [6 2 0]
     [7 3 0]]
'''

x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
              [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
'''
>>> [[[1 2 3]
      [4 5 6]
      [7 8 9]]

     [[10 11 12]
      [13 14 15]
      [16 17 18]]

     [[19 20 21]
      [22 23 24]
      [25 26 27]]]
'''

x.shape
'''>>> (3,3,3)'''

x[1:]
'''
>>> [[[1 2 3]
      [4 5 6]
      [7 8 9]]

     [[10 11 12]
      [13 14 15]
      [16 17 18]]]
'''

x[:, 1:]
'''
>>> [[[4 5 6]
      [7 8 9]]

     [[13 14 15]
      [16 17 18]]

     [[22 23 24]
      [25 26 27]]]
'''

x[:, :, ::2]
'''
>>> [[[1 3]
      [4 6]
      [7 9]]

     [[10 12]
      [13 15]
      [16 18]]

     [[19 21]
      [22 24]
      [25 27]]]
'''

# Broadcasting
x[x >= 26]  # Returns np array in 1-d that >=26
'''>>> [26 27]'''

x[x >= 26] = -1  # Mutates np array items satisfying this cond
x
'''
>>> [[[1 2 3]
      [4 5 6]
      [7 8 9]]

     [[10 11 12]
      [13 14 15]
      [16 17 18]]

     [[19 20 21]
      [22 23 24]
      [25 -1 -1]]]
'''

x / 100  # Return 3d np array st every item * 1/100 of before, note dtype becomes Float
'''
>>> [[[0.01 0.02 0.03]
      [0.04 0.05 0.06]
      [0.07 0.08 0.09]]

     [[0.1  0.11  0.12]
      [0.13 0.14 0.15]
      [0.16 0.17 0.18]]

     [[0.19  0.2   0.21]
      [0.22  0.23  0.24]
      [0.25 -0.01 -0.01]]]
'''

x * [1, 0, 0]  # Returns 3d np arrat st every slice * [1,0,0] point-wisely
'''
>>> [[[1 0 0]
      [4 0 0]
      [7 0 0]]

     [[10 0 0]
      [13 0 0]
      [16 0 0]]

     [[19 0 0]
      [22 0 0]
      [25 0 0]]]
'''

# Algebra

x = np.array([1, 2, 3])

x * 2
'''>>> [2 4 6]'''

x + 1
'''>>> [2 3 4]'''

x * x
'''>>> [1 4 9]'''

x @ x  #equivalent to sum(x*x), np.dot(x,x)
'''>>> 14'''

y = np.array(range(6)).reshape(2, -1)
y
'''
>>> [[0 1 2]
     [3 4 5]]
'''

y.T
'''
>>> [[0 3]
     [1 4]
     [2 5]]
'''

# Note when apply transpose to 1d array, nothing changes
z = np.array(range(10))
z.shape
'''>>> (10,)'''
z.T.shape
'''>>> (10,)'''