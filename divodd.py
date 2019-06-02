try:
	num=int(input())
	for i in range(1,num):
		div=num/i
		if(div%2==1):
			print(i)
			exit(0)
except ValueError:
	print("invalid")