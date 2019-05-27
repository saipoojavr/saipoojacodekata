try:
	number = int(input())  
	add = 0
	while number > 0:  
	   digit = number % 10  
	   add += digit ** 2  
	   number //= 10  
	print(add)
except ValueError:
	print("invalid")