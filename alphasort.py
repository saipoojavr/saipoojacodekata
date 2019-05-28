num=int(input())
arr=list(map(str,input().split()))
abc=sorted(arr,key=len)
for i in range(len(abc)-1):
    if len(abc[i])==len(abc[i+1]) and abc[i]>abc[i+1]:
        abc[i],abc[i+1]=abc[i+1],abc[i]
print(*abc)