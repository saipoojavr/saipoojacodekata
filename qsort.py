try:
	arrsize=int(input())
	arr=[int(x) for x in input().split()]
	print(*sorted(arr))
except ValueError:
	print("invalid")