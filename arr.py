try:
	arr_size=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,len(arr)):
		print(arr[i],i)
except ValueError:
	print("invalid")