try:
	num=int(input())
	arr=list(map(int,input().split()))
	prod=1
	for i in range(0,num):
		prod=prod*arr[i]
	if(prod%2==0):
		print("even")
	else:
		print("odd")
except ValueError:
	print("invalid")