try:
	number=int(input())
	exponent=int(input())
	print(pow(number,exponent))
except ValueError:
	print("invalid")