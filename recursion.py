def numbers(n):
	if(n>0):
		result = n + numbers(n-1)
		print(result)
	else:
		result = 0
	return result


numbers(10)