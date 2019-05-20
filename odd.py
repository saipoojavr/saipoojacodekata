try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	for iter in range(num1+1,num2):
		if(iter%2==1):
			print(iter,end=" ")
		else:
			continue
except ValueError:
	print("invalid")