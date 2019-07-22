try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,num):
		if arr[i]==max(arr[i::]):
			a.append(arr[i])
	print(*a)
	for i in range(num-1,-1,-1):
		if arr[i]==max(arr):
			print(arr[i],end=" ")
except ValueError:
	print("invalid")
