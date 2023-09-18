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

x = x.reshape(4, 2)
print("After resize is ")
print(x)
