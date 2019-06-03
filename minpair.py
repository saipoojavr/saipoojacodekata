try:
	num=int(input())
	arr=list(map(int,input().split()))
	count=0
	for i in range(0,num-1):
		for j in range(i+1,num):
			if(arr[i]<arr[j]):
				count+=1
	print(count)
except ValueError:
	print("invalid")