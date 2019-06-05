try:
	num=input()
	hex=int(num,16)
	print(hex)
except ValueError:
	print("invalid")	