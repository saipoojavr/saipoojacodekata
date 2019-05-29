try:
	arr_size,key=map(int,input().split())
	list=list(map(int,input().split()))
	for iter in list:
		if iter==key:
			print("yes")
			break
	else:
		print("no")
except ValueError:
	print("invalid")