astr=str(input())
for iter in range(0,len(astr)):
	if(astr[iter].islower()==True):
		print(astr[iter].upper(),end="")
	elif(astr[iter].isupper()==True):
		print(astr[iter].lower(),end="")