try:
	arrsize=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[1])
except ValueError:
	print("invalid")