try:
	num=int(input())
	count=0
	arr=[int(num) for num in input().split()]
	for i in range(1,1000):
	    for j in range(0,len(arr)):
	        if i%arr[j]==0:
	            count+=1
	            continue
	        else:
	            break
	    if count==num:
	        break
	    count=0
	print(i)
except ValueError:
	print("invalid")
