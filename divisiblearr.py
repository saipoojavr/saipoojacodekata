try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1):
		if(arr[i+1]%arr[i]==0):
			print(arr[i+1],end=" ")
except ValueError:
	print("invalid")
	