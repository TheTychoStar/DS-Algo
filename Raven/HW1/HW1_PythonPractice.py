#List
print('-----List-----')
sq = [0,1,4,9,16,25,36,49,64]

# for (i,item) in enumerate(sq, start=0):
#     print('{0}|{1}'.format(i,item))
for i in range(len(sq)):
    print('{}|{}'.format(i,sq[i]))
print('*'*50)

print(sq[0],sq[8],sq[-1])
print('*'*50)

print(len(sq))
print('*'*50)

sr = [x*x for x in range(9)]
print(sr)
print('*'*50)

one = sq + sr
two = one * 2
print(one)
print(two)
print('*'*50)

print(sq[:2])
print(sq[3:5])
print(sq[7:9])
print(sq[-8:-5])
print(sq[-3:])
print('*'*50)

#Queue and Stack
print('-----Queue and Stack-----')
q=[0,1,2,3,4,5]
print(q)

q.pop(0)
print(q)

q.append(0)
print(q)

q.pop(-1)
print(q)

q.pop(1)
print(q)

q = [1,2,5,3,4,7,6]
print('before sorting',q)
q.sort()
print('after sorting',q)

q = q[::-1]
print(q)

q = q[::2]
print(q)
print('*'*50)

#Deque - 'deck'
print('-----Deque-----')
from collections import deque

queue = deque(['three','four','five'])
print(queue)

queue.appendleft('two')
print(queue)

queue.extendleft('one')
print(queue)

queue.extendleft(['zero'])
print(queue)

queue.popleft()
print(queue)

queue.append('six')
print(queue)

queue.extend('seven')
print(queue)

queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.pop()
print(queue)

queue.append('seven')
print(queue)

queue.popleft()
queue.popleft()
queue.popleft()
print(queue)

print(queue.count('two'))

queue.reverse()
print(queue)

queue.rotate(1)
print(queue)

queue.rotate(-1)
print(queue)
print('*'*50)

#Dict
print('-----Dict-----')

D = {'name':'Bon','age':25,'job':'Dev','city':'New York'}

print(D['name'],D['age'],D['job'])

D['age'] += 1
print(D['age'])

D['email'] = 'bob@web.com'
print(D['email'])
print('*'*50)

cov19 = {'Toronto':96,'Ottawa':24,'Peel':296,'Waterloo':33,'Hamilton':23}

for k in cov19.keys():
    print('{}:{}'.format(k,cov19[k]))
for k,v in cov19.items():
    print('{:<9}:{:>5}'.format(k,v))
print('*'*50)

#Tree
print('-----Tree-----')
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

tr = TreeNode('A')

tr.left = TreeNode('B')
# tr.left.left = TreeNode('D')
# tr.left.right = TreeNode('E')
tr.right = TreeNode('C')
# tr.right.left = TreeNode('F')
# tr.right.right = TreeNode('G')

print(tr.val,tr.left.val,tr.right.val)

def DFS(tr):
    if tr == None:
        return
    print(tr.val)
    DFS(tr.left)
    DFS(tr.right)

DFS(tr)
print('*'*50)

#Numpy
print('-----Numpy-----')
import numpy as np

d = np.zeros(5)
print(d)

d = np.ones(5,dtype=int)
print(d)

d = np.array([1,2,3,4])
print(d)

d = np.empty(5)
print(d)

d = np.linspace(2,20,10)
print(d)

d2 = np.zeros([2,3], dtype=int)
print(d2)

d2 = np.array([[1,2,3],[4,5,6]])
print(d2)
print(d2.shape)

dr = np.random.randint(20,size=7)
print(dr)

dr = np.random.randint(5,15,size=[3,4])
print(dr)

dr = np.random.randint([0,10,100],[10,100,1000],size=(5,3))
print(dr)
print('*'*50)

#Slicing
print('-----Slicing-----')
print(dr[1:3])

print(dr[:,1:3])
print('*'*50)

#Pandas
print('-----Pandas-----')
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('https://data.ontario.ca/dataset/5472ffc1-88e2-48ca-bc9f-4aa249c1298d/resource/66d15cce-bfee-4f91-9e6e-0ea79ec52b3d/download/ongoing_outbreaks.csv')
print(df.head(10))
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.groupby(['outbreak_group']).sum())

dayct = df[['date','number_ongoing_outbreaks']].groupby(['date']).sum()
print(dayct)

print(dayct.plot(figsize=(15,7)))

