try:
	num1,num2=map(float,input().split())
	p=num1*num2
	print(format(p,".5f"))
except ValueError:
	print("invalid")