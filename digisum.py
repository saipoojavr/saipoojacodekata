try:
	num=int(input())
	sum=0
	r=0
	while(num>0):
		r=num%10
		sum=sum+r
		num=num//10
	print(sum)
except ValueError: 
	print("invalid")