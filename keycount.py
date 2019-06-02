# your code goes here
try:
	num1,num2=map(int,input().split())
	arr=list(map(int,input().split()))
	count=1
	for i in range(0,num1-1):
		for j in range(i+1,num1):
			if(arr[i]==arr[j]):
				count+=1
		if(count==num2):
			print(arr[i])
			count=1
		else:
			count=1
			continue
except ValueError:
	print("invalid")
