num=int(input())
arr=list(map(int,input().split()))
a=[]
for i in range(0,num-1):
	for j in range(i+1,num):
		s=arr[i]+arr[j]
		if(s<=0):
			a.append(s)
s1=min(a)
for i in range(0,num-1):
	for j in range(i+1,num):
		s2=arr[i]+arr[j]
		if(s2==s1):
			print(arr[i], arr[j])
			break
