import numpy as np
import pandas as pd

# DataFrame as a generalized NumPy Array
#
population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}
population = pd.Series(population_dict)

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
             'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)

states = pd.DataFrame({'population': population,
                       'area': area})
print(states)

# Constructoing DataFrame objects
print(pd.DataFrame(population, columns=['population']))

# From a dictionary of Series objects
print(pd.DataFrame(dict(population=population, area=area)))

# From an NumPy structured array
A = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
print(pd.DataFrame(A))

# Index as immutable array
ind = pd.Index([2, 3, 5, 7, 11])
print(ind[::2])

# Index as ordered set
indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
print(indA % indB)

# Series as dictionary
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])
print("data.keys(): ", data.keys())
print("list.(data.items()): \n", list(data.items()))

# Series as one-dimensional array
# slicing by explicit index
print("slicing by explicit index: \n", data['a':'c'])
# slicing by implicit integer index
print("slicing by implicit integer index: \n", data[0:2])
# masking
print(data[(data > 0.3) & (data < 0.8)])
# fancy indexing
print(data[['a', 'd']])

# Indexers: loc, iloc, and ix
data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
print(data)

# implicit index when slicing
print(data[1:3])
# loc
print("loc: ", data.loc[1])
