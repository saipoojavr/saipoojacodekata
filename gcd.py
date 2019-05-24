try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	m=max(num1,num2)
	c=0
	for i in range (1,m+1):
		if(num1%i==0 and num2%i==0):
			c=i
		else:
			continue
	print(c)
except ValueError:
	print("invalid")
	
		