try:
	num1,num2=input().split()
	num1=int(num1)
	num2=int(num2)
	temp=num1
	num1=num2
	num2=temp
	print(num1,num2)
except ValueError:
	print("invalid")