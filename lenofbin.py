try:	
	num=int(input())
	num1=bin(num)
	leng=num1[2:]
	print(len(leng))
except ValueError:
	print("invalid")