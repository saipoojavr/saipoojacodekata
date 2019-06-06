str1=input().split()
str2=input()
for i in range(0,len(str1)):
	if(str1[i]!=str2):
		print(str1[i],end=" ")
	else:
		continue