a = {
	
	"Name":"Azad",
	"Address":"Lucknow",
	"Mo.no":"8418826770"
	}							#Dictonary is unordered and doesn't allow duplicates. We can't access items using indexing.

print(a)
print(type(a))
print(len(a))

print(a["Name"])				#accessing the items using key

x = a.get("Address")
print(x)

y = a.keys()
print(y)

z = a.values()
print(z)

a["Education"] = "B.Tech"
print(a)

a["Mo.no"] = "8707794791"
print(a)

if "Education" in a:
	print("Exist")

a.update({"Mo.no":"8418826770"})
print(a)

a.pop("Education")
print(a)

a.popitem()
print(a)

del a["Address"]
print(a)

a.clear()
print(a)

del a

sampleDict = dict([
('first', 1),
('second', 2),
('third', 3)
])
print(sampleDict)

""" The get() method returns a value of key if the key is not found it returns None, instead of throwing a KeyError exception"""
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)