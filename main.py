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

# np.random.rand(n) returns n number of random values between 0 and 1
a = (np.random.rand(10))
print(a,end="\n\n")

#np.randome(n,o,p,....) returns a 3D array with n 2D arrays and o 3D arrays each with p elements

a = np.random.rand(2,3,4)
print(a,end="\n\n")

a = np.random.rand(2,3,4,5,6)
print(a,end="\n\n")

# to convert it to a range we can multiply it with a number and using np.round() on it
a = np.round((np.random.rand(10))*10) #returns numbers in range 0 to 10
print(a,end="\n\n")

# it generates samples from a standard normal distribution (mean = 0, standard deviation = 1). 
a = np.random.randn(10)
print(a,end="\n\n")

# np.zeros and np.ones creates a numpy array consisting of all elements 0 and 1 respectively
a = np.zeros(10,"i")
print(a,end="\n\n")
a = np.ones(10,"i")
print(a,end="\n\n")

# np.reshape reshapes the array to sepcified rows and columns
# the product of rows and columns have to be equal to the number of elements of the array

a = np.arange(100).reshape(2,5,10)
print(a,end="\n\n")


# in numpy slicing an array does not return a copy it accesses the same memory location so if you change the slice the original array will also change also known as shallow copy
# shallow copy is way faster and efficent than deep copies to acess data

a = np.arange(0,50)
b = a[3:10]
print(b,end="\n\n")

b[0] = 1000
print(a,end="\n\n")

