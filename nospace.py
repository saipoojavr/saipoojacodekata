astr=str(input())
for iter in range(0,len(astr)):
	if(astr[iter]==" " and astr[iter+1]==" "):
		print(" ",end="")
	elif(astr[iter]==" " and astr[iter-1]==" "):
		continue
	else:
		print(astr[iter],end="")
		
		
		
