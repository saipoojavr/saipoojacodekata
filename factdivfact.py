try:
	def fact(x):
		f=1
		for i in range(1,x+1):
			f=f*i
		return f
	num1,num2=map(int,input().split())
	print(fact(num1)//fact(num2))
except ValueError:
	print("invalid")