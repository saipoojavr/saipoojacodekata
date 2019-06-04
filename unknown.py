
try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for i in range(0,num):
		sum=sum+arr[i]
	print(sum*2)
except ValueError:
	print("invalid")