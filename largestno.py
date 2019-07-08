try:
	num=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	for i in range(len(arr),0,-1):
		print(i,end="")
except ValueError:
	print("invalid")
	