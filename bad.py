n,k=map(int,input().split())
s1=input()
list1=[int(x) for x in input().split()]
list2=[int(x) for x in input().split()]
s=[]
for iter in range(len(list2)):
	list1.append(list2[iter])
	x=max(list1)
	s.append(x)
print(*s)
	