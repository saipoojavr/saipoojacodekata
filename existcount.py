try:	
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	count=0
	for i in range(0,num1):
		if(arr[i]==num2):
			count+=1
	if(count>=1):
		print("yes",count)
	else:
		print("no")
except ValueError:
	print("invalid")