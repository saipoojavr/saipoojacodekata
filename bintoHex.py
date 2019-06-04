
num=input()
bin=int(num,2)
con=hex(bin)[2:]
a=""
for i in con:
	if i.isalpha():
		a=a+i.upper()
	else:
		a=a+i
print(a)