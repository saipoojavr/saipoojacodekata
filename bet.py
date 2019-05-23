try:
	num=int(input())
	n1,n2=input().split()
	n1=int(n1)
	n2=int(n2)
	if(num>n1 and num<n2):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")