try:
	n1,n2=map(int,input().split())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,n1):
		if(arr[i]%2==1):
			a.append(arr[i])
		else:
			continue
	print(a[n2-1])
except ValueError:
	print("invalid")