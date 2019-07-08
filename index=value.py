try:
	num=int(input())
	arr=list(map(int,input().split()))
	b=[]
	for i in range(0,len(arr)):
		if i==arr[i]:
			b.append(i)
	if len(b)==0:
		print("-1")
	else:
		print(*b)
except ValueError:
	print("invalid")
	
