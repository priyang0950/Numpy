from numpy import random 
a = random.randint(10) 
b= random.randint(50) 
print(a) 
print(b) 

#Numpy random to generate a list of float values 
from numpy import random 
a = random.rand() 
b= random.rand(5) 
print(a) 
print(b) 

#generate 3-dimensional arrays 
from numpy import random 
a = random.randint(10, size=(3,2,1)) 
print(a) 
from numpy import random 
a = random.randint(10, size=(3,2,2)) 
print(a) 

#we can generate multi-dimensional arrays using the choice() function by giving the size of the dimension. 
from numpy import random 
a = random.choice([8, 10, 16],size=(3, 2)) 
b= random.choice([80, 100, 160,1100],size=(5, 2)) 
print(a) 
print(b)