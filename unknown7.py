s=input()
count=0
for i in range(0,len(s)):
	if(s[i]=="0"):
		count+=1
if(count%2==0):
	print("yes")
else:
	print("no")