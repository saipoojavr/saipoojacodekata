try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	count=0
	for iter in range(num1,num2+1):
		if iter > 1: 
		   for iter1 in range(2, (iter//2)+1): 
		       if (iter % iter1) == 0: 
		           break
		   else: 
		       count=count+1 
		else: 
		   continue 
	print(count)
except ValueError:
	print("invalid")
