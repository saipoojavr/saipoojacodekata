try:	
	num=int(input())
	arr=list(map(int,input().split()))
	a=list(set(arr))
	a.sort(reverse=True)
	b=[]
	d=[]
	count=0
	for i in a:
		b.append(arr.count(i))
	while count<len(b):
		s=b.index(max(b))
		d.append(a[s])
		b[s]=0
		count+=1
	print(*d)
except ValueError:
	print("invalid")