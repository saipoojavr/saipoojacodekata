str1=input()
str2=input()
arr1=[]
arr2=[]
if (str1.isalpha() or " " in str1) and (str2.isalpha() or " " in str2):
    str1=list(str1.split(" "))
    str2=list(str2.split(" "))
    for i in str2:
        if str2.count(i) > str1.count(i) and i not in arr1:
            arr1.append(i)
    for i in arr1:
    	if(i!=" "):
    		print("1:"+i)
    for i in str1:
        if str1.count(i)>str2.count(i) and i not in arr2:
            arr2.append(i)
    for i in arr2:
    	if(i!=" "):
    		print("2:"+i)
else:
    for i in str2:
        if str2.count(i)>str1.count(i) and i not in arr1:
            arr1.append(i)
    for i in arr1:
    	if(i!=" "):
    		print("1:"+i)
    for j in str1:
        if str1.count(j)>str2.count(j) and j not in arr2:
            arr2.append(j)
    for i in arr2:
    	if(i!=" "):
    		print("2:"+i)