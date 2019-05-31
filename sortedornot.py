try:
	arr_size=int(input())
	arr=list(map(int,input().split()))
	arr1=sorted(arr)
	if(arr1==arr):
		print("yes")
	else:
		print("no")
except ValueError:
    print("invalid")