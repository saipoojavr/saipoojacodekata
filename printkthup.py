astr,num=input().split()
num=int(num)
for i in range(0,len(astr)):
	if((i+1)%num==0):
		print(astr[i].upper(),end="")
	else:
		print(astr[i],end="")

	