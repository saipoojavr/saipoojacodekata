try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,num-1):
		if(arr[i]>arr[i+1]):
			a.append(arr[i])
		else:
			a.append(arr[i+1])
	for iter in range(0,len(a)):
		print(a[iter],end=" ")
except ValueError:
	print("invalid")