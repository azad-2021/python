#eval() evaluates the string like a python expression and returns the result as an integer
#for accesing factorial(), we have to import math
import math

x = 3
y = eval('x**2+x-2')
print('result of eval function is: ',y,'\n' )

#len() returns the number of items in an object
numbers =  [1,2,3,4,5]
print('number list: ',numbers)
print('lenght of numbers: ', len(numbers), '\n')

#factorial funtion

a = math.factorial(10)
print('factorial of 10 is: ', a, '\n')

#sort() sorts the elements in accending or decendion order
a = [200,45,11,57,88,69,32]
print('a = :',a)
a.sort()
print('a in accending order: ', a)
a.sort(reverse = True)
print('a in decending order: ', a,'\n')

a=[23,2,13,56,34,34,1]

print(max(a))
#Desired output - 56
