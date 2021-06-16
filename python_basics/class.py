class NewClass:
	num = 10

p1 = NewClass()
print(p1.num)

#using _init_

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def hi(self):
		print('Hi!! this is ' + self.name)

ob1 = Person("Azad", 24)
ob1.hi()

print(ob1.name)
print(ob1.age)

#modify ob1 
ob1.age = 23
print(ob1.age)
del ob1.age			#deleting the object property "age"
del ob1				#deleting the whole object ob1