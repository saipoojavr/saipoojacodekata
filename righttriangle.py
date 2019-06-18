try:
	arr=list(map(int,input().split()))
	arr.sort()
	a=arr[0]
	b=arr[1]
	c=arr[2]
	if(c**2==a**2+b**2):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")