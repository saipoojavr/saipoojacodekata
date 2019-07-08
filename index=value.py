try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,len(arr)):
		if i==arr[i]:
			a.append(i)
	print(*a)
except ValueError:
	print("invalid")
	