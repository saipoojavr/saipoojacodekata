try:
	num=int(input())
	arr=[]
	for iter in range(2,num+1):
		if(num%iter==0):
			arr.append(iter)
	for i in range (0,len(arr)):
		if(arr[i]%2==0):
			print(arr[i],end=" ")
		else:
			continue
except ValueError:
	print("invalid")