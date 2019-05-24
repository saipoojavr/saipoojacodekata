astr=list(input())
l=len(astr)
for i in range(0,l):
	if(astr[i].isdigit()==True):
		print(astr[i],end="")
	else:
		continue