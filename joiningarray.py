#Joining Two or More Arrays 
import numpy as np
a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6]]) 
print ("concatenated array vertically:", np.concatenate((a, b), axis=0))
print ("concatenated array horizontally:", np.concatenate((a, b), axis=None))