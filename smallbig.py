try:
	num=int(input())
	arr=list(map(int,input().split()))
	count=1
	for i in range(0,num-2,2):
		if(arr[i]<arr[i+1]>arr[i+2]):
			count+=2
		elif(arr[i]>arr[i+1]<arr[i+2]):
			count+=2
		else:
			break
	if(count==num):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")