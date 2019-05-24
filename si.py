try:
	num1,num2,num3=map(int,input().split())
	print((num1*num2*num3)//100)
except ValueError:
	print("invalid")