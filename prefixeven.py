try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	for i in range(0,num):
		sum=sum+arr[i]
		if(sum%2==0):
			print(sum,end=" ")
		else:
			print(arr[i],end=" ")
except ValueError:
	print("invalid")