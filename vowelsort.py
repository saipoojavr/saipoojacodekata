arr=["a","e","i","o","u","A","E","I","O","U"]
num=int(input())
count=0
a=[]
for i in range(num):
	s=input()
	for i in s:
		if i in arr:
			count+=1
	a.append([s,count])
	count=0
a.sort(key=lambda x:x[1],reverse=True)	
for i in range(num):
    print(a[i][0])