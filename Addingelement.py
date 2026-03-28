#Adding Elements to an Existing Array 
import numpy as np
a = np.array([[1,2,3],[1,2,3]]) 
print ("array a is :", a) 
print ("array a after insertion:", np.insert(a,1,5, axis = 1)) 