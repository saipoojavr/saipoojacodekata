try:
	arrsize=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	print(max(arr))
except ValueError:
	print("invalid")