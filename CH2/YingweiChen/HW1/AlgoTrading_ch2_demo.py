import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io

image_file=r"D:\GoodDrive\PYTHON\AlgoTrade\Course Materials\Chapter2\beach.jpg"
image_beach=io.imread(image_file)
plt.imshow(image_beach)
image_beach.shape
print(image_beach[:2,:1])
#image_beach.show()

image_single_color=image_beach[:4045,:800]*np.array([1,1,1])
plt.imshow(image_single_color)

# Generate Some Random Number
Random_data=np.random.randn(2,3)
Random_data
Random_data_sq=Random_data*Random_data
Random_data_sq.shape


data_list1=[6,7,5,8,0,1]
data_list2=[1,2,3,4,5,6]
data_np=np.array(data_list1)
data_np
data_2d=[data_list1,data_list2]
data_np_2d=np.array(data_2d)
data_np_2d
data_np_2d.dtype
data_np_2d.shape

np.zeros([10,10])  # Generate 10*10 matrix with all elements Zeros
np.zeros(10)      # Generate array with 10 elements values 0

np.arange(10,101,5)  # from 10 to 100 by 5, 101 will not included
np.arange(10,20)    # from 10 to 20 by 1

arr1=np.array([1,2,3], dtype=np.float64)
arr1

#change string number to numerical number
numerica_str=np.array(['1.25','-9.6','42'], dtype=np.string_)
numerica_num=numerica_str.astype(np.float64)
numerica_num
#Note you can also use another object data type
