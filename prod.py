try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	if((num1*num2)%2==0):
		print("even")
	else:
		print("odd")
except ValueError: 
	print("invalid")