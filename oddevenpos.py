try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num):
		if(i%2==0):
			if(arr[i]%2==1):
				print(arr[i],end=" ")
		else:
			if(arr[i]%2==0):
				print(arr[i],end=" ")
except ValueError:
	print("invalid")