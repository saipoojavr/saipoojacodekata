st=str(input())
k=len(st)
if(k%2==0):
	for i in range(0,k):
		if(i==((k-1)//2) or i==(k//2)):
			print("*",end="")
		else:
			print(st[i],end="")
else:
	for i in range(0,k):
		if(i==(k//2)):
			print("*",end="")
		else:
			print(st[i],end="")