try:
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	print(arr[num2-1])
except ValueError:
	print("invalid")