try:
	num1,num2=map(int,input().split(" "))
	count=0
	for iter in range(num1,num2+1):
		for j in range(1,iter+1):
			if j**2==iter:
				count+=1
	print(count)
except ValueError:
	print("invalid")