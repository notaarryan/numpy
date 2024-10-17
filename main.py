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

#np.arange(start,stop,step)
a = np.arange(10,100) #creates a np array in the range[10,100) can have step value too
print(a,end="\n\n")

#np.random.permutatuon(iterable) aranges the elements of the iterable in a random order and returns a np array of it
a = np.random.permutation((1,2,3,4,5,6))
print(a,end="\n\n")

#returns a random interger in the provided range
# np.random.randint(low,high,size) if size is not specified it returns a number
#if size is specified it returns a np array
a = np.random.randint(0,20)
print(a,end="\n\n")