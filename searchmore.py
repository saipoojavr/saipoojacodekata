try:
	num,key=map(int,input().split())
	arr=list(map(int,input().split()))
	a=sorted(arr)
	for iter in range(0,num):
		if a[iter]==key:
			print(a[iter+1])
			break
	else:
		a.append(key)
		a.sort()
		for i in range(0,len(a)):
			if a[i]==key:
				print(a[i+1])
except ValueError:
	print("invalid")
