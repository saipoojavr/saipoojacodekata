try:
	num1,op,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	op=str(op)
	if(op=='/'):
		print(num1//num2)
	elif(op=='%'):
		print(num1%num2)
except ValueError:
	print("invalid")