astr=list(input().split())
arr=[]
a=""
for i in range(0,len(astr)):
	arr.append(sorted(astr[i]))
for i in arr:
	a+="".join(i)+" "
print(a.strip())

	