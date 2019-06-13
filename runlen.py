astr=str(input())
for i in range(1,len(astr)):
	if(astr[i].isdigit()==True):
		c=int(astr[i])
		for j in range(0,c):
			print(astr[i-1],end="")
