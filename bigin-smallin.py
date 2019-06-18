try:
	mum=int(input())
	arr=list(map(int,input().split()))
	a=max(arr)
	b=min(arr)
	print(abs(arr.index(a)-arr.index(b)))
except ValueError:
	print("invalid")