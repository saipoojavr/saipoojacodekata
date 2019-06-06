try:
	num1,num2=map(int,input().split())
	arr=[int(x) for x in input().split()]
	a=[]
	for i in arr:
		if arr.count(i)<num2:
			if i not in a:
				a.append(i)
	a.sort()
	print(*a)
except ValueError:
	print("invalid")
		