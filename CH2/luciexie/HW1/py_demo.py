print('--------List--------')
lst1 = [1,2,4,8,16,32]
print(lst1)
print(lst1 + lst1)
print(lst1*2)
lst2 = [888, 999, 555, 777]
lst1.append(lst2)
print(lst1)
lst3 = [1,2,4,8,16,32]
lst3.extend(lst2)
print(lst3)
lst3.pop()
print(lst3)
lst3.clear()
print(lst3)

print('-------Deque--------')
from collections import deque
dq1 = deque(['age', 'DOB', 'email'])
print(dq1)
dq1.append('phone')
print(dq1)
dq1.appendleft('name')
print(dq1)
dq1.extendleft('add')
print(dq1)
dq1.pop()
print(dq1)
dq1.popleft()
print(dq1)
dq1.popleft()
dq1.popleft()
print(dq1)
dq1.insert(4,'address')
print(dq1)
dq1.rotate(1)
print(dq1)
dq1.rotate(-3)
print(dq1)

print('-------Dictionary--------')
dict1 = {"brand": "Ford", "model": "Mustang", "year": 2000}
print(dict1)
print(dict1['model'])
dict1['colour'] = 'Black'
print(dict1)
for key in dict1:
    print("{:<6}: {:>7}".format(key, dict1[key]))


print('-------Tree--------')
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()  

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.PrintTree()

print('-------Numpy--------')
import numpy as np
zero1d = np.zeros(5)
print(zero1d)
zero2d = np.zeros([3,5], dtype=int)
print(zero2d)
randarr = np.random.randint(10, 50, size=9)
print(randarr)
randarr = np.random.randint(10, 50, size=[2,4])
print(randarr)
randarr = np.random.randint([0,10,10,1000], [100,1000,10000,100000], size=[6,4])
print(randarr)
print(randarr[3])
print(randarr[3:6])
print(randarr[:, 1:3])

arr = np.array([1, 2, 3])
arr2 = np.arry([20, 40, 60])
print(arr)
print(arr + arr2)
print(arr * arr2)
print(arr ** 2)
print(arr + 3)
print(arr.sum())

arr = np.array([[1, 2, 3], [8, 9, 10], [5, 7, 9], [8 ,1.3, 9.99]])
print(arr)
print(arr[:3, ::2])
arr = np.linspace(10,1000,8)
print(arr)
arr = np.arange(20)
print(arr)
print(arr[-8:15])
arr = np.arange(10, 1, -2)
print(arr)

print('-------Image--------')
from skimage import io
import matplotlib.pyplot as plt
img = io.imread('/Users/lhsieh/Documents/Documents/2015 Victoria/DCS_3414.JPG')
plt.imshow(img)
plt.show()
print(type(img))
print(img.shape)
print(img.dtype)
plt.imshow(img[:, ::-1])
plt.show()
plt.imshow(img[::-1, :, :])
plt.show()
plt.imshow(img[:, :, 0])
plt.show()
plt.imshow(img[790:2100, 3300:4050])
plt.show()
img_resize = img[::2, ::2]
plt.imshow(img_resize)
plt.show()
print(img_resize.shape)
plt.imshow(img[:, :, 1])
plt.show()
plt.imshow(img[:, :, 0].T)
plt.show()
img_masked = np.where(img>99, 255, 0)
plt.imshow(img_masked)
plt.show()
plt.imshow(img*[0,0,1])
plt.show()
plt.imshow(img/255*0.7)
plt.show()
img_32 = img // 32 * 32
plt.imshow(img_32)
plt.show()
plt.imshow(255-img)
plt.show()
img_dark = img*.5
plt.imshow(img_dark.astype('uint8'))
plt.show()
img_brgt = img * 2
img_brgt[img_brgt>255]=255
plt.imshow(img_brgt.astype('uint8'))
plt.show()
plt.imshow(img[::2, :, :])
plt.show()

print('-------Pandas--------')
import pandas as pd
# AMZN historical data
df = pd.read_csv('/Users/lhsieh/Documents/Documents/Python/DS-Algo/CH2/luciexie/HW1/AMZN.csv')
print(df.head())
print(df.dtypes)
print(df.size)
print(df.shape)
print(df[['Date', 'Open', 'Volume']])
print(df['Open'].max(), df['Open'].min())
masked = df['Open'] > df['Open'].median()
print(masked)
print(masked)
print(df.where(masked).dropna().head())