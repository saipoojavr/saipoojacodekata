try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	c=[]
	for i in range(1):
		for j in range(i,num):
			a.append(sum(arr[:j+1]))
	b=a[::-1]
	for i in range(num):
		c.append(str(a[i]+b[i]))
	print(" ".join(c))
except ValueError:
	print("invalid")