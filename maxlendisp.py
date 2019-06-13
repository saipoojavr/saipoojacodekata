astr=input()
a=[]
b=[]
for i in range(len(astr)):
		a.append(astr.count(astr[i]))
for i in range(len(astr)):
	if astr.count(astr[i])==max(a) and astr[i] not in b:
		b.append(astr[i])

print(max(a),"".join(b))