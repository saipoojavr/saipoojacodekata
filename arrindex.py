try:
	num=int(input())
	arr=[int(x) for x in input().split()]
	a=sorted(arr)
	b=[]
	for i in range(0,len(a)):
		for j in range(len(a)):
			if arr[i]==a[j]:
				b.append(j)
	for i in range(len(b)):
		b[i]=b[i]+1
	print(*b)
except ValueError:
	print("invalid")