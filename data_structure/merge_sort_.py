def merge_sort(arr):
	if len(arr) <= 1:			#return if list is empty or have only one element
		return
	mid = len(arr)//2 			#find the middle element in the list 
	left = arr[:mid]
	right = arr[mid:]

	merge_sort(left)			#calling function itself for dividing list again in two parts (recursion)
	merge_sort(right)

	merge_two_sorted_list(left, right, arr) 



def merge_two_sorted_list(a,b,arr):		# a = left, b = right
	len_a = len(a)
	len_b = len(b)

	i = j = k = 0

	while i <len_a and j < len_b:		
		if a[i] <= b[j]:
			arr[k] = a[i]
			i += 1
			k += 1
		else:
			arr[k] = b[j]
			j += 1
			k += 1
	while i < len_a:
		arr[k] = a[i]
		i += 1
		k += 1
	while j < len_b:
		arr[k] = b[j]
		j += 1
		k += 1


if __name__ == '__main__':
	
	arr = [10,3,15,7,8,23,98,29]

	test_cases = [

		[10,3,15,7,8,23,98,29],
		[],
		[3],
		[9,8,7,2],
		[1,2,3,4,5,6,7,8,9]

		]

	for arr in test_cases:
		merge_sort(arr)
		print(arr)