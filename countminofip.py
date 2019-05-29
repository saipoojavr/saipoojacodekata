try:
	num=int(input())
	count=0
	for iter in range(num):
		num1,num2=map(int,input().split())
		if num1<num2:
			count+=1
	print(count)
except ValueError:
	print("invalid")