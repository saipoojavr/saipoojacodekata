try:
	num=input()
	try:
	    int(num,16)
	    print("yes")
	except ValueError:
	    print("no")
except ValueError:
	print("invalid")