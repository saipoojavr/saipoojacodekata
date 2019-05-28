astr=str(input())
for iter in range(0,len(astr)):
	asc=ord(astr[iter])
	if(asc>=65 and asc<88):
		asc=asc+3
		print(chr(asc),end="")
	elif(asc==88):
		print('A',end="")
	elif(asc==89):
		print('B',end="")
	elif(asc==90):
		print('C',end="")
