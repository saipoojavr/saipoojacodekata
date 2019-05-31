try:
	peri,ar=map(int,input().split())
	h=int(peri/2)
	if(h*2==peri):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")