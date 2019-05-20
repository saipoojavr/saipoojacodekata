try:
	number=list()
	n1,l1 = input().split()
	l1 = int(l1)
	n1 = int(n1)
	add = 0
	number=input().split()
	for iter in range(0,l1):
	    add = add + int(number[iter])
	print (add)
except ValueError:
	print("invalid")