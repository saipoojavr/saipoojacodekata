try:
	n1 = input()
	s1 = list(map(int,input().split()))
	t1 = False
	for i in s1:
	    if s1.count(i) > 1:
	        t1 = True
	        break
	print(i if t1 else "unique")
except ValueError:
	print("invalid")