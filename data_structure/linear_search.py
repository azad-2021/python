a = [1,2,3,4,5,6,7,8,9]

for i in range(len(a)):
	if a[i]==9:
		print(i)
		break
	else:
		print('Element not found')


''' Looking for worst case, time complexity of linear search is O(n).
In larger data structures, we cann't use this algorithm '''