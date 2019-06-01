str1,str2=input().split()
for i in range(0,len(str1)):
	if str1[i]==str2[i]:
		print("yes")
		break
else:
	print("no")