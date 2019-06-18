try:
	n1,n2=map(int,input().split())
	if(n1%n2==0):
		print(n2)
	else:
		print(n1%n2)
except ValueError:
	print("invalid")