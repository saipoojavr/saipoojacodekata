try:
	num=int(input())
	iter=1
	while(num!=0):
		div=num/iter
		if(div%2==1):
			print(iter)
			break
		iter+=1
except ValueError:
	print("invalid")
	
