astr=input()
count=0
for i in range(0,len(astr)):
	if(astr[i].isdigit()==False):
		count=count+1
	else:
		continue
if(count!=0):
	print("no")
else:
	print("yes")