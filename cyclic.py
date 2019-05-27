try:	
	num1,num2 = map(int,input().split())
	num2 = num2%num1
	list1 = list(map(int,input().split()))
	list2 = list1[-num2:] + list1[:-num2]
	print(*list2)
except ValueError:
	print("invalid")