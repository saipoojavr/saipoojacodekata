try:
	number=int(input())
	factorial=1
	for iter in range(1,number+1):
		factorial*=iter
	print(factorial)
except ValueError:
	print("invalid")