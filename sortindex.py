try:
	num=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c=sorted(b)
	d=[]
	for i in c:
	    j=b.index(i)
	    d.append(a[j])	
	print(*d)
except ValueError:
	print("invalid")
	