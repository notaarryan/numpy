import numpy as np

# np.array returns a numpy array
# numpy array can only store elements of same datatypes
#you can also specify the datatype of numpy array 
#np.array(iterable,"datatype")
a = np.array([[[2,1],[1,2]],[[2,3],[3,2]]]) 
#all nested lists need to have same number of elements
b = np.array((2,3,4,5))

print(a,end="\n\n")
print(a.ndim,end="\n\n") #prints the dimension of the np array
print(a.shape,end="\n\n") #prints the number of 2D,3D... arrays
print(a.size, end="\n\n") #prints the number of elements in the array
print(b.nbytes,end="\n\n") #prints the number of bytes this array takes
print(b.dtype,end="\n\n") #prints the data type of the elements