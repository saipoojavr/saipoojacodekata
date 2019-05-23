try:
	number=int(input())
	if number > 1: 
	   for iter in range(2, number//2): 
	       if (number % iter) == 0: 
	           print("no") 
	           break
	   else: 
	       print("yes") 
	else: 
	   print("no") 
except ValueError:
	print("invalid")