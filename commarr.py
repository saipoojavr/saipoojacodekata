try:
	num=int(input())
	list3=[]
	s=""
	list1=list(map(int,input().split()))
	list2=list(map(int,input().split()))
	for i in list1:
		if i in list2 and i not in list3:
			list3.append(i)
	for i in list3:
		s=s+str(i)+" "
	print(s.strip())	
except ValueError:
	print("invalid")
