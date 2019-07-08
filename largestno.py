try:
	num=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	c=0
	for i in range(0,num):
		if(arr[i]==0):
			c+=1
	if(c==num):
		print("0")
	else:
		for i in range(len(arr)-1,-1,-1):
			print(arr[i],end="")
except ValueError:
	print("invalid")
	
