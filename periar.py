try:
	peri,ar=map(int,input().split())
	h=int(peri/2)
	if(h*2==peri):
		if ar > 1:
			for iter in range(2, ar//2):
				 if (ar % iter) == 0: 
				 	print("yes")
				 	break
			else:
				print("no")
		else:
			print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")
	
