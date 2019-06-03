try:
	num=int(input())
	arr=list(map(int,input().split()))
	a=[]
	if num==1:
		print(arr[0])
	else:
		for i in range(num-1):
			a.append(arr[i]|arr[i+1])
		print(max(a))
except ValueError:
	print("invalid")
