# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:49:52 2020

@author: Songbin Zhang
"""
print ("=====list======")
num = [      [0 for i in range(1,5)]   for j in range(1,5)   ]
print(num)  # 打印数组
print("-"*50)  


print ("=====deque======")
from collections import deque
queue=deque(["three","four","five"])
print (queue)
queue.appendleft("two")
print (queue)
queue.extendleft("one")
print (queue)
queue.extendleft(["zero"])
print (queue)
queue.popleft()
print (queue)
queue.append("six")
print (queue)
queue.extend("seven")
print (queue)
queue.popleft(),queue.popleft(),queue.popleft()
print (queue)
queue.pop(),queue.pop(),queue.pop(),queue.pop()
print (queue)
queue.pop()
print (queue)
print (queue.count("two"))
queue.reverse()
print (queue)
queue.rotate(1)
print (queue)
queue.rotate(-2)
print (queue)


print ("=====dick======")
cov19={"Toronto":96,
       "Ottawa":24,
      "Peel":296,
      "Waterloo":33,
      "Hamilton":23}
print (cov19)
for k in cov19.keys():
    print ("{}:{}".format(k,cov19[k]))
for k,v in cov19.items():
    print ("{:<9}:{:>5}".format(k,v))
    
print ("=====tree======")
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
tr=TreeNode("A")
print (tr)
tr.left=TreeNode("B")
tr.right=TreeNode("C")
print (tr.val)
print (tr.left.val)
print (tr.right.val)
print ("-"*10)
def DFS(tr):
    if (tr==None):
        return
    print (tr.val)
    DFS(tr.left)
    DFS(tr.right)
DFS(tr)
    
print ("=====numpy======")
import numpy as np
d=np.zeros(5)
print (d)
d=np.ones(5,dtype=int)
print (d)
d=np.array([1,2,3,4])
print (d)
d=np.empty(5)
print (d)
d=np.linspace(2,20,10)
print (d)
d2=np.zeros([2,3],dtype=int)
print (d2)
d2=np.array([[1,2,3]  ,  [4,5,6]])
print (d2)
print (d2.shape)

dr=np.random.randint(0,20,size=7)
print (dr)
dr=np.random.randint(5,15,size=[3,4])
print (dr)
dr=np.random.randint([0,10,100],[10,100,1000],size=[9,3])
print (dr)
print (dr[1:3])
print (dr[:,  1:3 ])

print ("=====panda======")
import pandas as pd
df=pd.read_csv("https://data.ontario.ca/dataset/5472ffc1-88e2-48ca-bc9f-4aa249c1298d/resource/d5d8f478-765c-4246-b8a7-c3b13a4a1a41/download/outbreak_cases.csv")
print (df.head())
print (df.shape)
print (df.columns)
print (df.dtypes)
print (df.groupby(["category_grouped"]).sum())
dayct=df[["date","TOTAL_CASES"]].groupby(["date"]).count()
print (dayct)
print ("-"*20)
dayct=df[["date","TOTAL_CASES"]].groupby(["date"]).sum()
print (dayct)
print (dayct.plot(figsize=(15,7)))
df.groupby(["category_grouped"]).sum().plot.pie(
    y="TOTAL_CASES",autopct="%1.1f%%",textprops={"color":"b"},figsize=(10,10))



print ("=======iamge==========")
from skimage import io
import matplotlib.pyplot as plt
canvasSize=(13,11)
jpg=io.imread("206.jpg")
print(type(jpg))
print (jpg.shape)
plt.imshow(jpg)

plt.imshow(jpg[:,::-1])
plt.imshow(jpg[1000:1300  , 1000:2000])
plt.imshow(jpg[::2, ::2])
print (jpg.shape)
plt.imshow(jpg[:,  :, 1 ])
plt.imshow(jpg[:,:,0].T)
jpg_masked=np.where(jpg>99,255 ,0)
plt.imshow(jpg_masked)
plt.imshow(jpg/255*0.7)
jpegex=jpg/255*1.5
jpegex[jpegex>255]=255
plt.imshow(jpegex)
plt.imshow(jpg*[1,0,0])
plt.imshow(jpg*[-1,-1,-1]+255)


print ("=======Algebra==========")
a=np.array([1,3,5,7])
b=np.array([2,4,6,8])
print (a+b)
print (a*2)
print (a*b)
print (a@b)
print (np.dot(a,b))
dr=np.random.randint(10,size=7)
print (dr[dr>5])





