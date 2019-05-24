astr=str(input())
l=len(astr)
count=0
for i in range(0,l):
	if(astr[i].isdigit()==True):
		print(astr[i],end="")
		count=count+1
	else:
		continue
if(count==0):
	print(astr,end="")
