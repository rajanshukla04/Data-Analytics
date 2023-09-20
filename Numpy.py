import numpy
import numpy as np

a = np.array([(1, 2, 3), (4, 5, 6)])
print(a.ndim)
print(a.size)

print("shape of array ", a.shape)
# Single dimanesson array
a = np.array([1, 2, 3, 4, 5])
print(a.ndim)
print(a.size)  # toatl number present in the array
print(a.dtype)

# shape of array


print(a.shape)

# REshape and Sciling

x = np.array([(1,2,3,4),(5,6,7,9)])
print("Original array shape ")
print(x)
#
# x = x.reshape(4, 2)
# print("After resize is ")
# print(x)


print(x[0,2])
print("all remove ")
print(x[0:,3])


#linespace

a=numpy.linspace(1, 3, 10)
print(a)

print("Element has maximum value ",x.max())

print("minumim value ", x.min())



# summ of all axis element

print(x)
print(x.sum(axis=0))  #axis is zero list sum of axis
print(x.sum(axis=1))   # axis of clolum wise


# seqaure root of each elelment

print(np.sqrt(x))

# standarded deveation

# standard deviction tell about the
print((np.std(x)))



# sum of two array

a=np.array([(1,2,3),(4,5,6)])
b=np.array([(1,2,3),(4,5,6)])

print("Arithmatic of two array")
print(a+b)
print(a-b)
print((a*b))
print(a/b)

#stacking the array

print(np.hstack((a,b)))

print(np.vstack((a,b)))


# array to list
print(a.ravel())





