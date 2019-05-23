try:
	num=int(input())
	for iter in range(0,1000):
	    if 2**iter==num:
	        break
	iter=iter+1
	print(2**iter)
except ValueError:
	print("invalid")
