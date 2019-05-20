import statistics
try:
	n = input()
	arr = list(map(int, input().split()))
	arr.sort()
	print(statistics.median(arr))
except ValueError:
	print("invalid")