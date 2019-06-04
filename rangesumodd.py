try:
	num1,num2=map(int,input().split())
	sum=0
	for i in range(num1,num2+1):
		if(i%2==1):
			sum=sum+i
		else:
			continue
	print(sum)
except ValueError:
	print("invalid")