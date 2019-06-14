b=input()
deci=int(b,2)
temp=deci
while 1:
	if temp&(temp-1):
		temp=temp+1
	else:
		print(temp)
		break