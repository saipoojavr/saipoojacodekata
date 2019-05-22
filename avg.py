try:
	arrsize=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for iter in range(0,arrsize):
		sum=sum+arr[iter]
	print(sum//arrsize)
except ValueError:
	print("invalid")