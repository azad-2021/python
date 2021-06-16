'''Important functions in numpy
import numpy as numpy		#importy numpy as np
np.sin(arr)
np.cos(arr)
np.log(arr)
np.mean(arr)
np.median(arr)
np.std(arr) 			#for standard deviation
np.exp(arr)
np.a(n)					#n = number of dimension, a = number 
#ie np.ones(2)			#creates 1-d array of ones
np.zeros((2,2))			#creates 2-d array of zerosarr = np.eye(2,2)
arr = np.eye(2,2)		#creates 2-d identity array
arr.reshape()			#reshape funtion


where arr is an array variable
'''

import numpy as np

#Zero Dimensional Array
zero_D_array = np.array(30)
print(zero_D_array)

#1-D Array or 1st order Tensor
one_D_array = np.array([1, 2, 3, 4, 5])
print(one_D_array)
print("1st element", one_D_array[0])
print("2nd element", one_D_array[1])
print("3rd element", one_D_array[2])
print("\n")
#2-D Array or 2nd order Tensor
two_D_array = np.array([[1, 2, 3, 4, 5], [6, 7 ,8, 9,10]])	#1st Dimension has index [0] and second has index [1] 
print(two_D_array)
print("1st element of 1st dimension", two_D_array[0,0])
print("2nd element of 1st dimension", two_D_array[0,1])
print("3rd element of 1st dimension", two_D_array[0,2])
print("4th element of 1st dimension", two_D_array[0,3])
print("1st element of 2nd dimension", two_D_array[1,0])
print("2nd element of 2nd dimension", two_D_array[1,1])
print("3rd element of 2nd dimension", two_D_array[1,2])
print("4th element of 2nd dimension", two_D_array[1,3])
print("\n")

three_D_array = np.array([[[1, 2, 3, 4, 5], [6, 7 ,8, 9,10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])	#1st Dimension has index [0] and second has index [1] 
print(three_D_array)
print("\n")
print("1st element of 1st array", three_D_array[0,0,0])
print("2nd element of 1st array", three_D_array[0,0,1])
print("3rd element of 1st array", three_D_array[0,0,2])
print("1st element of 2nd array", three_D_array[0,1,0])
print("2nd element of 2nd array", three_D_array[0,1,1])
print("3rd element of 2nd array", three_D_array[0,1,2])
print("1st element of 3rd array", three_D_array[1,0,0])
print("2nd element of 3rd array", three_D_array[1,0,1])
print("3rd element of 3rd array", three_D_array[1,0,2])
print("1st element of 4th array", three_D_array[1,1,0])
print("2nd element of 4th array", three_D_array[1,1,1])
print("3rd element of 4th array", three_D_array[1,1,2])
print("\n")
print(np.__version__)
print(type(three_D_array))

print("Dimension:",zero_D_array.ndim)				#zero_D_array.ndim will return dimension in integer
print("Dimension:",one_D_array.ndim)
print("Dimension:",two_D_array.ndim)
print("Dimension:",three_D_array.ndim)
print("\n")
#higher dimension array
a = np.array([1,2,3,4], ndmin = 5)
print(a)
print("Dimension of a:",a.ndim)



#slicing of arrays
b = np.array([1,2,3,4,5], ndmin = 1)
print(b)
print(b[1:4])
print(b[2:])
print(b[:3])
print(b[0:4:2])
print("\n")

#slicing 2-d array
c = np.array([[1, 2, 3, 4, 5], [6, 7 ,8, 9,10]])
print(c)
print(c[1,1:4])				#prints 2 to 4 elements in 2nd array
print(c[0:2,3])				#prints 4th element of 1 to 2 array
print('\n')
print(c[0:2,1:4])

'''
Data type in numpy
i-integer		b-boolean		u-unsigned integer			f-float					c-complex float							m-time delta

M-datetime		O-object		S-string					U-unicode string		v-fixed chunk memory for other type
'''

d = np.array([1,2,3,4,5], ndmin = 1)
e = np.array(["Delhi","Mumbai", "Kolkata", "Chennai"])
f = np.array(["Delhi","Mumbai", "Kolkata", "Chennai"], dtype = "S")
print(d.dtype)
print(e.dtype)
print(f.dtype)

#Mathematical operations using arrays
g = 2 + d
print(g)

h = np.array([10,20,30,40,50], ndmin = 1)
i = d + h
j = d*h
print(i)
print(j)

k = np.dot(d,h)			#dot product
#l = np.cross(d,h)
print(k)
#print(l)

m = np.exp(h)
print(m)

print(np.zeros((2,2)))

arr = np.eye(2,2)			#creates 2-d identity array
print(arr)

h = np.array([84.3,24.2,30,43.2,2.5], ndmin = 1)
print(h)

hr = np.round(h)			#round off float values. "np.round(h,n)" where n = number of allowe digits to round off
print(hr)

b = np.array([6.999245,240.6624,18.12452])
br = np.round(b,2)
print(br)

arr = np.linspace(0,10,5) #generates an evenlt spaced numbers over a specified interval by first two arguments of the function
#and third argument specify the number of samples to be generated
print(arr,'\n')


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr,'\n')

newarr = arr.reshape(4, 3)	#By reshaping we can add or remove dimensions or change number of elements in each dimension.

print(newarr)