try:
	n1,n2=map(int,input().split())
	num=n1^n2
	con=bin(num)[2::]
	c=0
	for i in range(0,len(con)):
		if(con[i]=="1"):
			c+=1
	print(c)
except ValueError:
	print("invalid")