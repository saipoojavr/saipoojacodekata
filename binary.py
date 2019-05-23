num=str(input())
count=0
for i in range(0,len(num)):
	if (num[i]=='0' or num[i]=='1'):
		continue
	else:
		count=count+1
if(count>0):
	print("no")
else:
	print("yes")