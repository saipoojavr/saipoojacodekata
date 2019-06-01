num=int(input())
astr=input()
a1=""
c1=""
for i in range(len(astr)):
	if astr[i]=="1":
		a1=a1+astr[i]+" "
	elif astr[i]=="0":
		c1=c1+a1
		a1=""
print(c1.strip())