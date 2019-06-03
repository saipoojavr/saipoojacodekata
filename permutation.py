try:	
	def fact(a):
		f=1
		for i in range(1,a+1):
			f=f*i
		return(f)
	n,r=map(int,input().split())
	num=fact(n)
	deno=fact(n-r)
	print(num//deno)
except ValueError:
	print("invalid")