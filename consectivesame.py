num=int(input())
arr=[]
count=0
for i in range(0,num):
	arr.append(input())
for iter in range(0,num-1):
	if(arr[iter]==arr[iter+1]):
		count+=1
if(count>0):
	print("yes")
else:
	print("no")
