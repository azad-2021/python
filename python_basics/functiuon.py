def fun(name):

	print("Hello " + name)

fun("Azad")


def function(name = "Professor"):
	print("Hello " + name)

function()					#if calling function with empty argument, it will take default value set when defining the function
function("Azad")


def city(city):
	for i in city:
		print(i)

a = ['Delhi', 'Mumbai', 'Kolkata', 'chennai']
b = ('Delhi', 'Mumbai', 'Kolkata', 'chennai')
c = {'Delhi', 'Mumbai', 'Kolkata', 'chennai'}
print(type(a))									#passing list as argument 
print(type(b))									#passing tuple as argument
print(type(c))									#passing set as argument
print('List :')
city(a)
print('tuple :')
city(b)
print('set :')
city(c)


def allType(List,Tuple,Set):					#passing argument as List, Tuple and Set at a time
	print("List :")
	for i in List:
		print(i)
	print('tuple :')
	for j in Tuple:
		print(j)
	print('set :')
	for k in Set:
		print(k)

allType(a,b,c)



def data(*name):
	print(name[1])

data("jaipur", "jaisalmer", "Banglore")


#Lambda function


x = lambda i : i + 10								#calling lambda function >>> x(10)

print("Lambda function x output is " + str(x(10)))

y = lambda i,j : i*j
print("Lambda function y output is " + str(y(10,10)))		#calling lambda function >>> y(10,10)

z = lambda i,j,k : i*j+k
print("Lambda function z output is " + str(z(10,10,20)))	#calling lambda function >>> z(10,10,20)

#Lambda functiuon within a function

def calculate(n):
	return lambda x: x*n

double = calculate(2)
triple = calculate(3)

#calling lambda function
print(double(10))
print(triple(30))