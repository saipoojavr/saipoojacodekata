astr=input().split()
for i in range(1,len(astr)):
	if(astr[i]=="and"):
		temp=astr[i-1]
		astr[i-1]=astr[i+1]
		astr[i+1]=temp
for j in range(0,len(astr)):
	print(astr[j],end=" ")
		