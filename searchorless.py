try:
	num,key=map(int,input().split())
	arr=list(map(int,input().split()))
	a=sorted(arr)
	for iter in a:
		if iter==key:
			print(key)
			break
	else:
		a.append(key)
		a.sort()
		for i in range(0,len(a)):
			if a[i]==key:
				print(a[i-1])
except ValueError:
	print("invalid")