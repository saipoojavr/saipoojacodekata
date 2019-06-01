astr,ch=map(str,input().split())
count=0
for i in range(0,len(astr)):
	if(astr[i]==ch):
		count+=1
	else:
		continue
print(count)