try:
	num=int(input())
	if(num%7==0):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")
