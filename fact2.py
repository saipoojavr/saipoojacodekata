try:
	number=int(input())
	factorial1=1
	for iter in range(1,number+1):
		factorial1*=iter
	print(factorial1)
except ValueError:
	print("invalid")
