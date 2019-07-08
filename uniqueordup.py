try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in arr:
		if arr.count(i)>1:
			if i not in a:
				a.append(i)
	print(*a)
	if len(a)==0:
		print("unique")
except ValueError:
	print("invalid")
	