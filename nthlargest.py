try:
	n1,n2=map(int,input().split())
	arr=list(map(int,input().split()))
	arr1=sorted(arr)
	print(arr1[n1-n2])
except ValueError:
	print("invalid")