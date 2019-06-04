try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for i in range(0,num-1):
		sum=sum+arr[i]+arr[i+1]
	print(sum)
except ValueError:
	print("invalid")