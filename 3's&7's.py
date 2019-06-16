try:
	num=int(input())
	count=0
	for i in range(0,num+1):
		if(i*3==num):
			count+=1
		elif(i*7==num):
			count+=1
		elif(i*3+i*7==num):
			count+=1
	if(count>=1):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")