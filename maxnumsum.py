try:
	num=int(input())
	arr=list(map(int,input().split()))
	sum=0
	a=[]
	for i in range(0,num-1):
		if(arr[i]<arr[i+1]):
			a.append(arr[i+1])
		else:
			a.append(arr[i])
	for j in range(0,len(a)):
		sum=sum+a[j]
	print(sum)
except ValueError:
	print("invalid")
