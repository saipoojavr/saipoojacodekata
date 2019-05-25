try:
	n1,n2=map(int,input().split())
	arr=list(map(int,input().split()))
	arr.sort()
	print(arr[n2-1])
except ValueError:
	print("invalid")
