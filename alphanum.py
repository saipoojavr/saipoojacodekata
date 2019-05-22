string=str(input())
count=0
count1=0
for iter in range(0,len(string)):
	if(string[iter].isalpha()==True):
		count=count+1
	elif(string[iter].isdigit()==True):
		count1=count1+1
	else:
		continue
if(count>0 and count1>0):
	print("Yes")
else:
	print("No")
