a = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'] #creating list
print(len(a))		#lenght of list
print(a.count('Delhi'))	#for counting how many times items in the list
print(a.index('Chennai'))	#printing the index of kolkata
print('\n',a[::-1],'\n')	#printing list in reverse order


for city in a:   # Printing list
	print(city)
if "Delhi" in a:  # checking if item is avilable in list or not
	print("Delhi is in List")
a[1] = "Lucknow"   # changing the item of list using indexing
print(a)

a[0] = ['Jaipur', 'Kanpur'] #Adding list in list
print(a)
print(a[0][0])   			#Accessing item of list in list 

a.insert(1,'Chandigrah')	#insert item with indexing
print(a)

a.append('Varangal')		# insert item in the end of the list
print(a)

b = ['Gorakhpur', 'Sidharth Nagar'] # creating a new list

a.extend(b)                       #adding list b in the end of list a
print(a)
print("\njoining two list\n")
print(a+b,'\n')			#joining two list

a.remove('Sidharth Nagar')		 #Remove perticular item
print(a)

a.pop(1)						#Remove items with indexing
print(a)

a.pop()							#remove last item in the list
print(a)

del a[0]						#another way to remove item with indexing
print(a)

print(b)
b.clear()
print('list b is now empty\t')
print(b)

del b						#remove the whole list
print('list b is deleted')
#print(b)                        if we use print(b) it will print error

c = list(a)						# copy the list
print(c)


aList = [1, 2, 3, 4, 5, 6, 7]
pow2 =  [2 * x for x in aList]
print(pow2)

sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

b = list(('Haryana', 'rajasthan', 'Andhra Pradesh'))   #list constructor
print(b)


print(b[-1])												
print(b[-2])

print(a[0:2])				#print form o to n-1 index
print(a[:2])				#print from start to n-1 
print(a[1:])				#print from 1 to last 

z = [6, 3, 4, 1, 2, 7, 5]	#sorting list
z.sort()
print(z)