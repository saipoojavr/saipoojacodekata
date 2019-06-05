try:
	num,m=map(int,input().split())
	arr=list(map(str,input().split()))
	a=[]
	b=arr[:num]
	c=arr[num:]
	for i in c:
	    if i in b:
	        a.append(i)
	a.sort()
	print(" ".join(a))
except ValueError:
	print("invalid")