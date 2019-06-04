try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	a=[]
	for i in range(0,num):
		sum=sum+arr[i]
		a.append(sum)
	print(*a)
except ValueError:
	print("invalid")