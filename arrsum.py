try:
	arrsize=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for i in range(0,arrsize):
		sum=sum+arr[i]
	print(sum)
except ValueError:
	print("invalid")