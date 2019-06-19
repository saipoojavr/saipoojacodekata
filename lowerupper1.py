str1=str(input())
for iter in range(0,len(str1)):
	if(str1[iter].islower()==True):
		print(str1[iter].upper(),end="")
	elif(str1[iter].isupper()==True):
		print(str1[iter].lower(),end="")