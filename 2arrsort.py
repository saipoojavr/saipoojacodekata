try:
	num1,num2=map(int,input().split())
	arr1=list(map(int,input().split()))
	arr2=list(map(int,input().split()))
	a=arr1+arr2
	a=sorted(a)
	print(*a)
except ValueError:
	print("invalid")