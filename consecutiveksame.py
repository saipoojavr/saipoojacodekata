num1,num2=map(int,input().split())
arr=[]
count=1
for i in range(0,num1):
	arr.append(input())
for iter in range(0,num1-1):
	if(arr[iter]==arr[iter+1]):
		count+=1
if(count==num2):
	print("yes")
else:
	print("no")
