str1=input()
str2=input()
arr=[]
if (str1.isalpha() or " " in str1) and (str2.isalpha() or " " in str2):
    str1=list(str1.split(" "))
    str2=list(str2.split(" "))
    for i in str1:
        if str1.count(i) > str2.count(i) and i not in arr:
            arr.append(i)
    for i in str2:
        if str2.count(i)>str1.count(i) and i not in arr:
            arr.append(i)
    print(*arr)
else:
    for i in str1:
        if str1.count(i)>str2.count(i) and i not in arr:
            arr.append(i)
    for j in str2:
        if str2.count(j)>str1.count(j) and j not in arr:
            arr.append(j)
    print(*arr)