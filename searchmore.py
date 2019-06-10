try:
	num,key=map(int,input().split())
	arr=list(map(int,input().split()))
	a=sorted(arr)
	for i in range(0,len(a)):
		if a[i]==key:
			print(a[i+1])
except ValueError:
	print("invalid")