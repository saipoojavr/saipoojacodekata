astr=input()
astr.split()
astr=astr.replace(" ","")
b=[i for i in astr if astr.count(i)==1]
arr=' '.join(b)
print(arr)
