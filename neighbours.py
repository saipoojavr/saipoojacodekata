try:	
	n,k=map(int,input().split())
	s=[[abs(i-k),i]for i in list(map(int,input().split()))]
	s.sort()
	s=s[1:]
	t=[i[1] for i in s[:3]]
	print(*t,sep=' ')
except ValueError:
	print("invalid")