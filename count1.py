try:
	num=int(input())
	arr=list(map(int,input().split()))
	for iter in arr:
	    if arr.count(iter)==1:
	        print(iter)
except ValueError:
	print("invalid")