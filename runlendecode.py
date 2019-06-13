astr=input()
a=[]
for i in range(0,len(astr)):
    if astr[i] not in a:
        a.append(astr[i])
        a.append(astr.count(astr[i]))
for i in range(0,len(a)):
    print(a[i],end="")