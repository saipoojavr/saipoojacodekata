try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1):
		if(arr[i+1]-arr[i]==1):
			print("yes")
			break
		else:
			print("no")
			break
except ValueError:
	print("invalid")
	