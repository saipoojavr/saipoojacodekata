try:	
	num=int(input())
	arr=list(map(int,input().split()))
	count=1
	temp=count
	f=1
	for i in range(num-1):
		if arr[i]==arr[i+1]:
			count+=1
			f=count
		elif count>temp:
			temp=count
			f=count
			count=1
	print(f)
except ValueError:
	print("invalid")