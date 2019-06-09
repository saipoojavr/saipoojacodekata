astr=input()
count=0
for i in range(0,len(astr)):
	if(astr[i]=="a" or astr[i]=="b"):
		count+=1
if(count==len(astr) or count==len(astr)-1):
	print("yes")
else:
	print("no")