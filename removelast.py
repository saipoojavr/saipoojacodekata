try:	
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	for i in range(0,num1-num2):
		print(arr[i],end=" ")
except ValueError:
	print("invalid")