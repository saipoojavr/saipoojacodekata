try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in arr:
		if arr.count(i)==1:
			print(i)
except ValueError:
	print("invalid")
	