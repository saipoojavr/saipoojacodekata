try:
	num=int(input())
	if(num%2==0):
		print(num)
	else:
		print(num-1)
except ValueError: 
	print("invalid")