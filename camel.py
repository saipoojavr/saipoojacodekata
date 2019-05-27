astr=str(input())
print(astr[0].upper(),end="")
for i in range(1,len(astr)):
	if(astr[i-1]==" "):
		print(astr[i].upper(),end="")
	else:
		print(astr[i].lower(),end="")
