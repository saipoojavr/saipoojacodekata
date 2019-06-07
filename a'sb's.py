astr=input()
count=0
for i in range(0,len(astr)):
	if(astr[i]=="a" or astr[i]=="b"):
		count+=1
if(count==len(astr)):
	print("yes")
else:
	print("no")