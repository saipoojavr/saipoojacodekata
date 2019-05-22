try:
	arrsize=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[0],end=" ")
	print(arr[-1],end=" ")
except ValueError:
	print("invalid")