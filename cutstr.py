str1,str2=input().split()
a=len(str1)
b=len(str2)
str3=""
if(a<b):
	for i in range(0,a):
		str3=str3+str2[i]
	print(str1+str3)
elif(a>b):
	for j in range(0,b):
		str3=str3+str1[j]
	print(str3+str2)
elif(a==b):
	print(str1+str2)
	