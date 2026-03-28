#Deleting the Elements from an Array 
import numpy as np
a = np.array([[1,2,3],[1,2,3]])
print ("array a is :", a) 
print ("after deletion:", np.delete(a, 1, axis=0))
