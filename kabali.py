num=int(input())
arr=[]
asc=0
count=0
for i in range(num):
    c=input()
    arr.append(c)
for i in arr:
	for j in i:
		asc+=ord(j)
	if(asc==612):
		count+=1
	asc=0
print(count)
			