str1=input()
a=[]
for i in str1:
	if i not in a:
		a.append(i)
for i in a:
	print(i,end="")