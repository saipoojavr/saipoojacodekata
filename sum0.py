try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1):
		for j in range(i+1,num):
			s=arr[i]+arr[j]
			if(s==0):
				print(arr[i], arr[j])
				break
except ValueError:
	print("invalid")