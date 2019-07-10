try:
	s=input()
	h=1
	for d in range (len(s)-1):
	  ph=s[d]+s[d+1]
	  m=int(ph)
	  if m<=26 and s[d]!="0":
	      h+=1
	if h==3:
	  print(h)
	else:
	  print(h+(h-1)//2)
except ValueError:
	print("invalid")