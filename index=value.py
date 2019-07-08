try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in range(0,len(arr)):
		if i==arr[i]:
			a.append(i)
	if len(a)==0:
		print("-1")
	else:
		print(*a)
except ValueError:
	print("invalid")
	
