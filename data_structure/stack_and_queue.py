#Stack
#When function calls another function then the details of previous function are stored in Stack
#First in last out principle
print('stack implementation\n')
letters = []		#empty list

#push operation in stack using append method
print('adding items in stack')
letters.append('a')
letters.append('b')
letters.append('c')
letters.append('d')
print(letters,'\n')

#removing elements / pop operation of stack
print('removing items from stack')
letters.pop()
print(letters)

letters.pop()
print(letters)

letters.pop()
print(letters,'\n')

#implementing queue using list
#First in First out principle
print('Queue implementation\n')1
#element is inserted at one end called Rear and deleted at other end called Front.

Cities = []
#enqueue operation / adding items in queue
print('Enqueue operation\n')

Cities.append('Delhi')
Cities.append('Mumbai')
Cities.append('Kolkata')
Cities.append('chennai')
print(Cities,'\n')

#deleting items from queue / dequeue operation
print('dequeue operation\n')

Cities.pop(0)
print(Cities)
Cities.pop(0)
print(Cities)
Cities.pop(0)
print(Cities,'\n')

