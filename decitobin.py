try:
	num=int(input())
	print(bin(num)[2:])
except ValueError:
	print("invalid")