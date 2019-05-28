astr=str(input())
for iter in range(0,len(astr)):
	asc=ord(astr[iter])
	asc=asc+3
	print(chr(asc),end="")