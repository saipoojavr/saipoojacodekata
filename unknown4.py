num1,num2=map(int,input().split())
c=0
for i in range (0,num3):
	n1,n2=map(int,input().split())
	if(abs(n1[i]-n2[i])==1):
		c+=1
print(c)
