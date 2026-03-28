#Copying from One Array to Another 
import numpy as np
a=np.array([1,2],dtype=int) 
print(a)
a1=np.array([3,4],dtype=int)
print(a1)

c=np.array([a,a1])
print("new array:",c)




zeros_array = np.zeros([2,2], dtype = int) 
print ("Array zeros is:", zeros_array) 
ones_array = np.ones([2,2], dtype = int) 
print ("Array ones is :", ones_array) 

np.copyto(zeros_array,ones_array) 
print ("New zeros array :", zeros_array)
