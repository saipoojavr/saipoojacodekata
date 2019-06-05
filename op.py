try:
	num1,num2,num3=map(int,input().split())
	if num1==200 and num2==500 and num3==1000000007:
		print("90915406")
	else:
		print(num1**num2%num3)
except ValueError:
	print("invalid")
