try:
	n1,n2=input().split()
	n1=int(n1)
	n2=int(n2)
	p=n1*n2
	sq=p**0.5
	if sq**2==p:
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")
