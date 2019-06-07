try:	
	num=int(input())
	con=bin(num)[2::]
	c=0
	for i in range(0,len(con)):
		if(con[i]=="1"):
			c+=1
	print(c)
except ValueError:
	print("invalid")
			
