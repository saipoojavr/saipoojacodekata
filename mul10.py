try:
	num=int(input())
	for i in range(num+1,num+11):
		if(i%10==0):
			print(i)
		else:
			continue
except ValueError:
	print("invalid")
