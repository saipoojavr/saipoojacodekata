try:	
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	a=sorted(arr[0:num2])
	b=sorted(arr[num2:])
	c=a+b[::-1]
	print(*c)
except ValueError:
	print("invalid")