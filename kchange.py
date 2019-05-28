str1,str2,num=input().split()
str1=str(str1)
str2=str(str2)
num=int(num)
count=0
for i in range(0,len(str1)):
	if(str1[i]!=str2[i]):
		count+=1
	else:
		continue
if(count==num):
	print("yes")
else:
	print("no")