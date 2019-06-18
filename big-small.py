try:
	mum=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[-1]-arr[0])
except ValueError:
	print("invalid")