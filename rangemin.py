try:
	num1,num2,num3=map(int,input().split())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(num2-1,num3):
		a.append(arr[i])
	print(min(a))
except ValueError:
	print("invalid")
	
		