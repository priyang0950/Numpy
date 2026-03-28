#1.numpy.around() 
import numpy as np 
a = np.array([1.0,5.55, 123, 0.567, 25.532]) 
print(np.around(a)) 
print( np.around(a, decimals = 1) ) 
print (np.around(a, decimals = -1)) 

#2.numpy.floor() 
import numpy as np  
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])    
print (a)  
print ('The modified array:')  
print (np.floor(a))  

#3.numpy.ceil()
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])  
print ('The given array:')  
print (a)  
print (np.ceil(a)) 

#4.numpy.rint()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.rint(a)   
print("Output array:",a1)   

#5.numpy.sum()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.sum(a)   
print("Output array:",a1) 

#6.numpy.average()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.average(a)   
print("Output array:",a1) 

#7.numpy.mean()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.mean(a)   
print("Output array:",a1) 

#8.numpy.min()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.min(a)   
print("Output array:",a1) 

#9.numpy.max()
import numpy as np 
a = [0.23, 0.09, 1.2, 1.24, 9.99]   
print("Input array:",a)   
a1 = np.max(a)   
print("Output array:",a1) 