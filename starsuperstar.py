try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num):
		if arr[i]==max(arr[i::]):
			print(arr[i],end=" ")
	print("\r")
	for i in range(num-1,-1,-1):
		if arr[i]==max(arr):
			print(arr[i],end=" ")
except ValueError:
	print("invalid")