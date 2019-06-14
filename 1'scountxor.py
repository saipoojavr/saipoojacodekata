try:
	num1,num2=map(int,input().split())
	xor=num1^num2
	con=bin(xor)[2:]
	c=0
	for i in range(0,len(con)):
		if(con[i]=="1"):
			c+=1
	print(c)
except ValueError:
	print("invalid")
	