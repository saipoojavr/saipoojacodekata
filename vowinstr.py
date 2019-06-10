num=int(input())
arr=[]
for iter in range(num):
    arr.append(input())
if all("a" in iter or "e" in iter or "i" in iter or "o" in iter or "u" in iter for iter in arr):
    print("yes")
else:
    print("no")