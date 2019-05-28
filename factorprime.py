try:
	num=int(input())
	arr=[]
	for iter in range(2,num+1):
		if(num%iter==0):
			arr.append(iter)
	for i in range (0,len(arr)):
		if arr[i] > 1: 
		   for j in range(2, (arr[i]//2)+1): 
		       if (arr[i] % j) == 0: 
		           break
		   else: 
		       print(arr[i],end=" ") 
		else: 
		   continue 
except ValueError:
	print("invalid")