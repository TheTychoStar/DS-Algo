from collections import deque
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import zipfile


# list
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
print(list1[3:8])
print(list1[3:8:2])  # 2 is step size
print(list1[-6:-2])
print(list1[:])
print(list1[::])
print(list1[::2])   # 2 is step size

# -1 is step size from backward, this will make the whole list inverse
print(list1[::-1])
print(list1[::-2])   # -1 is step size from backward

list2 = [x for x in range(5)]
print(list2)

list3 = [x**2 for x in range(5)]
print(list3)

list4 = [x*3 for x in range(10) if x*3 > 5]
print(list4)

print(list4.count(27))

print(list4.index(27))

print(list4[-1])

# Mutable objects are modified in place. Examples: lists, dictionaries.
# Immutable objects return new instances
# when methods are called on them. Examples: tuples, strings.

list4.reverse()
print(list4)


# deque
queue = deque(['bob', 'tom', 'kate'])
print(queue)

queue.append('marry')
print(queue)

queue.appendleft('gary')
print(queue)

queue.extend('jerry')
print(queue)

queue.extend(['stephen'])
print(queue)

queue.reverse()
print(queue)

queue.rotate(5)
print(queue)

queue.reverse()
print(queue)

# temp=(queue.popleft(),
#       queue.popleft(),
#       queue.popleft(),
#       queue.popleft(),
#       queue.popleft())
print(queue.popleft(),
      queue.popleft(),
      queue.popleft(),
      queue.popleft(),
      queue.popleft())
print(queue)

print(queue.pop())
print(queue)

# Dict
D = {'name': 'bob', 'height': 170, 'weight': 130, 'country': 'CA'}
print(D)
print(type(D))
print(D.keys())
print(D.items())
print(D['name'], D['country'])
D['weight'] += 1
print(D['weight'])

for k in D.keys():
    print("{}:{}".format(k, D[k]))

for k, v in D.items():
    print("{:<9}:{:>5}".format(k, v))
# <9  ====>> lenght = 9 alignment from right side
# >5  ====>> lenght = 5 alignment from left side


# Tree
# Definition for a binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


tr = TreeNode('A')
print(tr)

tr.left = TreeNode('B')
tr.right = TreeNode('C')
print(tr, tr.left, tr.right)
print(tr.val, tr.left.val, tr.right.val)


def DFS(tr):
    if tr is None:
        return
    print(tr.val)
    DFS(tr.left)
    DFS(tr.right)


print(DFS(tr))

# Numpy
# Numpy Arrays are mutable
# the contents of a Numpy array are homogenous(the same data type)
d = np.zeros(5)
print(d)
print(type(d[0]))

d = np.zeros(5, dtype=int)
print(d)
print(type(d[0]))

d = np.ones(5, dtype=int)
print(d)

d = np.array([1, 2, 3, 4])  # initialized from a python list
print(d)
print(type(d))
print(d.dtype)
print(type(d[0]))

d = np.empty(5)    # without initializaion
print(d)
print(d.dtype)

d = np.linspace(2, 20, 10)   # from 2 to 20, 10 elements
print(d)
print(d.dtype)

d = np.linspace(3, 29, 10)
print(d)
print(d.dtype)

d2 = np.zeros([5, 4], dtype=int)
print(d2)
print(d2.dtype)

d2 = np.array([[1, 2, 3], [4, 5, 6]])
print(d2)
print(d2.dtype)
print(d2.shape)

# create 7 rand int between[0, 20)
dr = np.random.randint(20, size=7)
print(dr)
print(dr.dtype)
print(dr.shape)

# create 6 row , 5 column numpy array , between[3, 15)
dr = np.random.randint(3, 15, size=[6, 5])
print(dr)
print(dr.dtype)
print(dr.shape)

# lower bound and upper bound could be more flexiable
dr = np.random.randint([0, 10, 100], [10, 100, 1000], size=[5, 3])
print(dr)

# numpy array slicing
# print(dr[-1])
print(dr[:-1])
# print(dr[1:3])
# print(dr[:,1:3])

canvasSize = (13, 11)
jpg = io.imread('orca.jpg')
print(type(jpg))
print(jpg.shape)
plt.figure(figsize=canvasSize)
plt.imshow(jpg)
# the 1st : means no change on the 1st dimension,
# the -1 means step size = 1 , but reverse order
# plt.imshow(jpg[::-1])

# the 1st : means no change on the 1st dimension,
# ::-1  means change the 2nd dimension(right <=> left)
# plt.imshow(jpg[:,::-1])
# plt.imshow(jpg[0:400,400:600])
# plt.imshow(jpg[::2,::2])
# plt.imshow(jpg[:,:,0:1])   # fetch RED degree[0-255]
# plt.imshow(jpg[:,:,1:2])   # feteh BLUE degree[0-255]
# plt.imshow(jpg[:,:,2:3])    # fetch GREEN degree[0-255]
# print(jpg[1,1,:])       #[163 209 243]
# print(jpg[100,100,:])   #[ 79 159 220]
# plt.show()


# Algebra
a = np.array([1, 3, 5, 7])
b = np.array([2, 4, 6, 8])
print(a)
print(b)
print(a + 10)
print(a + b)
print(a * 2)
print(a * b)
print(a @ b)
print(np.dot(a, b))

x = np.arange(6).reshape((3, 2))    # numpy.reshape(a, newshape, order='C')
print(x)
print(x.T)    # transpose, change the shape
print(np.transpose(x))
x = np.ones((1, 2, 3))    # numpy.ones(shape, dtype=None, order='C')
print(x)
print(x.shape)
print(type(x.shape))    # the value of a shape is <class 'tuple'>
print(np.transpose(x, (1, 0, 2)).shape)

print(jpg[:, :, 0].shape)
print(jpg[:, :, 0].T.shape)
# plt.imshow(jpg[:,:,0].T)
# plt.show()

# numpy.random.randint(low, high=None, size=None, dtype=int)
dr = np.random.randint(10, 20, size=7)
print(dr)
dr = np.random.randint(10, size=7)
print(dr)

print(type(dr.sort()))
dr.sort()       # Numpy Arrays are mutable
print(dr)
print(dr > 5)
print(dr[dr > 5])

jpg_masked = np.where(jpg > 99, 255, 0)    # if > 99. set to 255, else 0
# plt.imshow(jpg_masked)
# plt.show()

# Broadcasting
print(jpg.shape)  # (939, 1240, 3)
print(jpg[0:3, 0:3])
# plt.imshow(jpg/255 * .7)   # become much more dark
# plt.imshow(jpg/255 * 1.5)   # become much more bright
# plt.show()

jpgex = jpg/255 * 1.5
jpgex[jpgex > 1] = 1
print(jpgex[0:3, 0:3])
# plt.imshow(jpgex)
# plt.show()

# plt.imshow( jpg *[1, 0, 0])   # only fetch RGB - RED channel
# plt.imshow( jpg *[0, 1, 0])   # only fetch RGB - GREEN channel
print(jpg[0:3, 0:3])
print(jpg[0:3, 0:3] * [0, 0, 1])
# plt.imshow( jpg *[0, 0, 1])   # only fetch RGB - BLUE channel
# plt.show()

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# ValueError: operands could not be broadcast together with shapes(3,)(2,)
# c = np.array([3, 4])
c = np.array([3])
print(a + b)
print(a + c)

print(jpg[0:3, 0:3])
# print(jpg[0:3, 0:3] *[-1, -1, -1] + 255)
print(255 - jpg[0:3, 0:3])
# plt.imshow( jpg *[-1, -1, -1] + 255 )  # contrast copy
plt.imshow(255 - jpg)  # contrast copy - alternative
plt.show()


# Pandas
url = 'https://www.cftc.gov/files/dea/history/com_disagg_xls_2020.zip'
r = requests.get(url, allow_redirects=True)

open('com_disagg_xls_2020.zip', 'wb').write(r.content)
myzip = zipfile.ZipFile('com_disagg_xls_2020.zip')
xlfile = myzip.open('c_year.xls')
df = pd.read_excel(xlfile)
print(df.shape)
df1 = df.iloc[:, 0:19].copy()
print(df1.head())

y = ["PALLADIUM - NEW YORK MERCANTILE EXCHANGE",
     "PLATINUM - NEW YORK MERCANTILE EXCHANGE",
     "SILVER - COMMODITY EXCHANGE INC.",
     "GOLD - COMMODITY EXCHANGE INC."]

for x in y:
    df3 = df1.loc[df['Market_and_Exchange_Names'] == x]
    # print(df3.Market_and_Exchange_Names)
    df3 = df3.reset_index(drop=True)
    plt.figure(figsize=(24, 5))
    plt.title(x + '   M_Money_Positions in 2020')
    plt.plot(df3.Report_Date_as_MM_DD_YYYY,
             df3.M_Money_Positions_Long_ALL,
             'r.-',
             label='Long')
    plt.plot(df3.Report_Date_as_MM_DD_YYYY,
             df3.M_Money_Positions_Short_ALL,
             'b.-',
             label='Short')
    plt.plot(df3.Report_Date_as_MM_DD_YYYY,
             df3.M_Money_Positions_Long_ALL - df3.M_Money_Positions_Short_ALL,
             'g.-',
             label='Net')
    plt.xticks(df3.Report_Date_as_MM_DD_YYYY, rotation=90)
    plt.legend()
    plt.show()
