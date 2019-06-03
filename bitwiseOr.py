try:
	num=int(input())
	arr=[int(x) for x in input().split()]
	a=arr[0]
	for i in range(1,len(arr)):
		a=a|arr[i]
	print(a)
except ValueError:
	print("invalid")