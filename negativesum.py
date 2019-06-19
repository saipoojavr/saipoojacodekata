try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for i in arr:
		if i<0:
			sum=sum+i
	print(sum)
except ValueError:
	print("invalid")