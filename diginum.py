try:
	num=int(input())
	r=0
	count=0
	while(num>0):
		r=num%10
		count=count+1
		num=num//10
	print(count)
except ValueError:
	print("invalid")