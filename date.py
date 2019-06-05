try:
	date=input()
	length=len(date)
	date=list(map(int,date.split("/")))
	if length!=10:
	    print("no")
	else:
	    print("yes" if ((date[0]<=31) and (date[1]<=12)) else "no")
except ValueError:
	print("invalid")