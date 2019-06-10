num1,num2=map(int,input().split())
arr=[]
count=0
vow=["a","e","i","o","u"]
for i in range(num1):
    arr.append(input())
for i in arr:
	if any(j in i for j in vow):
		count+=1
if count>=num2:
    print("yes")
else:
    print("no")