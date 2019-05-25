astr,n=input().split()
astr=str(astr)
n=int(n)
for iter in range(0,len(astr)):
	if(iter==len(astr)-n):
		for j in range(iter,len(astr)):
			print(astr[j],end="")
	else:
		continue
	