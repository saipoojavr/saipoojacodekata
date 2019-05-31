# your code goes here
astr,num=map(str,input().split())
num=int(num)
length=len(astr)
temp=astr
for i in range(0,num):
	temp=temp[-1]+temp[:length-1]
print(temp)