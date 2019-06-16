try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	for i in arr:
		if i not in a:
			if arr.count(i)==1:
				a.append(i)
	if(len(a)==len(arr)):
		print("1")
	else:
		print(len(arr)-len(a))
except ValueError:
	print("invalid")