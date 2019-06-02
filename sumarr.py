try:
	arr_size,sum=map(int,input().split())
	arr=[int(x) for x in input().split()]
	for i in range(0,arr_size):
		for j in range(i+1,arr_size):
			if arr[i]+arr[j]==sum:
				print("yes")
				exit(0)
	print("no")
except ValueError:
	print("invalid")