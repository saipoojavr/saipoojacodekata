try:
	number=int(input())
	tempo=number
	rever=0
	while tempo != 0:
		rever=(rever*10)+(tempo%10)
		tempo=tempo//10
	if number==rever:
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")