try:
	num1,num2=map(int,input().split())
	print(pow(num1,num2))
except ValueError:
	print("invalid")