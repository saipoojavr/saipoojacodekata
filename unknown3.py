try:
	n,k=map(int,input().split())
	arr=[]
	count=0
	for i in range(0,n):
	    arr.append(list(map(int,input().split())))
	for i in range(0,len(arr)):
	    if arr[i][1]==k:
	        count+=1
	if count==0:
	    print("no")
	else:
	    print("yes")
except ValueError:
	print("invalid")
