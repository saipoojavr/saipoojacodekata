try:
	number=int(input())
	add=0
	for iter in range(0,number+1):
		add=add+iter
	print(add)
except ValueError:
	print("invalid")
