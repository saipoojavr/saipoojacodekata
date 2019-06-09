astr=input().split()
for i in range(0,len(astr)):
	if(i==0 or i==len(astr)-1):
		print(astr[i],end=" ")
	else:
		print(''.join(reversed(astr[i])),end=" ")
	