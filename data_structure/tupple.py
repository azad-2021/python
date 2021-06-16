a = ('Delhi', 'Mumbai', 'Kolkata', 'Chennai', 'Delhi')
print(a)			#since a has duplicate value of Delhi, Tuple allow duplicate values. 
print(type(a))
print(len(a))		#length of tuple
print(a.count('Delhi'))	#for counting how many times items in the tuple
print(a.index('Chennai'))	#printing the index of kolkata

print('\n',a[::-1],'\n')	#printing tuple in reverse order
b = ('Jaipur',)    #adding "," after "jaipur" create tuple with single item. if "," is not added then it will consider as string.
print(b)
print(type(b))

b = tuple(('Haryana', 'rajasthan', 'Andhra Pradesh'))   #tuple constructor
print(b)

print(a+b)			#joining two tuples

print(b[0])												#Accesing items with index

print(b[-1])												
print(b[-2])

print(a[0:2])				#print form o to n-1 index
print(a[:2])				#print from start to n-1 
print(a[1:])				#print from 1 to last 

if "Delhi" in a:  # checking if item is avilable in tuple or not
	print("Delhi is in Tuple")				

#Because tuple is imutabele, if we want to change items we have to convert tuple into list. After updating, convert back into tuple.

print(a)
a_list = list(a)				#convert tuple into list
a_list[1] = "Jaipur"			#update item in the list
a = tuple(a_list)				#convert back list into tuple
print(a)								


aTuple = "Yellow", 20, "Red"
a, b, c = aTuple
print(a)


t=(100,200)

print(t*2) 				#prints (100,200,100,200)
print(type(t))