try:
	arrsize,key=input().split()
	arrsize=int(arrsize)
	key=int(key)
	array=list(map(int,input().split()))
	count=0
	for iter in range(0,arrsize):
		if(array[iter]==key):
			count=count+1
		else:
			continue
	if(count>=1):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")