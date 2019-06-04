num=input()
count=1
for i in range(0,len(num)-1):
	for j in range(i+1,len(num)):
		if(num[i]==num[j]):
			count+=1
if(count>1):
	print("yes")
else:
	print("no")