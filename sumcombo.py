try:
	num=int(input())
	arr=list(map(int,input().split()))
	for i in range(0,num-1):
		for j in range(i+1,num):
			s=arr[i]+arr[j]
			if s in arr and arr[i]<arr[j]<s:
				print(str(arr[i])+" "+str(arr[j])+" "+str(s),"\r")
except ValueError:
	print("invalid")