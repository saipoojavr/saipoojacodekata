try:
	number=int(input())
	if number > 1: 
	   for iter in range(2, number//2): 
	       if (number % iter) == 0: 
	           print("yes") 
	           break
	   else: 
	       print("no") 
	else: 
	   print("yes") 
except ValueError:
	print("invalid")