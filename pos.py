try:
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	for i in range(0,num1):
		if(arr[i]==num2):
			print(i+1)
except ValueError:
	print("invalid")