astr=input()
s=""
for i in astr:
	if astr.count(i)>1:
		s+=i.upper()
	else:
		s+=i
print(s)