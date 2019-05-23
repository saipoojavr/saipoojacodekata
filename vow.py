s1=str(input())
count=0
for i in range(0,len(s1)):
	if(s1[i]=='a'or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u'):
		count=count+1
	else:
		continue
if(count>0):
	print("yes")
else:
	print("no")