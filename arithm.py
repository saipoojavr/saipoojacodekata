try:
	a,d,n=input().split()
	n = int(n)
	a = int(a)
	d = int(d)
	total = (n * (2 * a + (n - 1) * d)) // 2
	print(total)
except ValueError:
	print("invalid")