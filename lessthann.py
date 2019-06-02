try:
	num1=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,num1):
		if(arr[i]<num1):
			a.append(arr[i])
	a.sort()
	for i in range(0,len(a)):
		print(a[i],end=" ")
except ValueError:
	print("invalid")