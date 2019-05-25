try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1):
		if(arr[i]>arr[i+1]):
			print(i)
		else:
			continue
except ValueError:
	print("invalid")