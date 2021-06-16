a = {'Delhi', 'Mumbai', 'Kolkata', 'Chennai'}	#set items are unordered, unchangeable and don't allow duplicate values
print(a)										#Everytime we run script, set prints the value in different order
print(type(a))
print(len(a))

b = set(('Haryana', 'rajasthan', 'Andhra Pradesh'))   #set constructor
print(b)

for x in a:						#accessing values from set
	print(x)


print('Haryana' in b)			#check item is in set or not

#Below are two methods of adding items in sets
a.add('jaipur')				
a.update(['Varangal'])
print(a)

a.remove('Varangal')		#it give error if item is unavialable
a.discard('jaipur')
a.discard('Andhra')			#it don't get error even if there in item is unavialable in set. As example Andhra is not in sets.
print(a) 

a.clear()					#for deleting all items in set
print(a)

del a						#for deleting whole set

set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}
 
set1.difference_update(set2)
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}
 
print(set1.issubset(set2))
print(set2.issuperset(set1))

set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}
 
set3 = set1.union(set2)
print(set3)


sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red"])
print(sampleSet,'\n')

#union method
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print('union of set1 and set2 :',set1|set2)
print('union of set1 and set2 :',set1.union(set2),'\n')

#Intersection method
print('intersection of set1 and set2 :',set1&set2)
print('intersection of set1 and set2 :',set1.intersection(set2),'\n')

#set difference
# The difference of set B from A is is the set of elements which are present in only A not in B and vice versa
A = {1,2,4,6}
B = {1,4,8,9}
print('Difference of A and B :',A-B)
print('Difference of A and B :',A.difference(B),'\n')
print('Difference of B and A :',B-A)
print('Difference of B and A :',B.difference(A),'\n')

#The set symmetric difference is the set of all elements from A and B excluding elements that are common in both
print('Symmetric Difference of A and B :',A^B)
print('Symmetric Difference of A and B :',A.symmetric_difference(B),'\n')

s={2,5,7,2,8}

print(s.issubset(s))