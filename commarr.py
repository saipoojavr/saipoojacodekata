try:
	num=int(input())
	arr1=list(map(int,input().split()))
	arr2=list(map(int,input().split()))
	for i in range(0,len(arr1)):
		for j in range(0,len(arr2)):
			if(arr1[i]==arr2[j]):
				print(arr1[i],end=" ")
except ValueError:
	print("invalid")