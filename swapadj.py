try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1,2):
		temp=arr[i]
		arr[i]=arr[i+1]
		arr[i+1]=temp
	print(*arr)
except ValueError:
	print("invalid")