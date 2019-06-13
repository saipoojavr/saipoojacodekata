n1,n2=map(int,input().split())
g=min(n1,n2)
c=1
for i in range(1,g+1):
	c*=i
print(c)
