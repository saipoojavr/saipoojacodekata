try:
	num=int(input())
	arr1=list(map(int,input().split()))
	arr2=list(map(int,input().split()))
	arr1.reverse()
	if(arr1==arr2):
		print("yes")
	else:
		print("no")
except ValueError:
	print("invalid")