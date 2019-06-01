try:
	arrsize,num=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[num-1])
except ValueError:
	print("invalid")