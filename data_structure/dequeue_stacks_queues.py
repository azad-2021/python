from collections import deque

#initialing
print('Stack implementation using deque module')
numbers = deque()

#push method
print('push method')
numbers.append(21)
numbers.append(25)
numbers.append(13)
numbers.append(10)

print(numbers,'\n')

print('pop method')
numbers.pop()
print(numbers)
numbers.pop()
print(numbers,'\n')

#initialing
print('queue implementation using deque module')
Cities = deque()

#enqueue operation / adding items in queue
print('Enqueue operation\n')

Cities.append('Delhi')
Cities.append('Mumbai')
Cities.append('Kolkata')
Cities.append('chennai')
print(Cities,'\n')

print('Dequeue operation')
Cities.popleft()
print(Cities)
Cities.popleft()
print(Cities,'\n')