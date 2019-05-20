try:
	number=int(input())
	for iter in range(1,6):
		print(number*iter,end=" ")
except ValueError:
	print("invalid")