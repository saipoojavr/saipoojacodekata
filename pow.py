try:
	number,exponent=input().split()
	number=int(number)
	exponent=int(exponent)
	print(number**exponent)
except ValueError:
	print("invalid")
