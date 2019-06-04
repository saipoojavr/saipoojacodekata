try:
	num=int(input())
	arr=[int(x) for x in input().split()]
	a=set(arr)
	b=sorted(a)
	print(*b)
except ValueError:
	print("invalid")