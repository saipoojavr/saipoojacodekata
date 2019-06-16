try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in arr:
		a.append(arr.count(i))
	print(max(a))
except ValueError:
	print("invalid")