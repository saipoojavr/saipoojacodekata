try:
	n1,n2,n3=map(int,input().split())
	print(n1*n3+n2)
except ValueError:
	print("invalid")
