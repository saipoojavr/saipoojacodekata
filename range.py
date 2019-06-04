try:
	num,k=input().split()
	k=int(k)
	count=0
	for i in range(k+1):
		if str(i) in num:
			count=1
		else:
			count=0
			break
	if count==1:
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")